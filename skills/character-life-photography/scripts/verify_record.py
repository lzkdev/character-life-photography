#!/usr/bin/env python3
"""Check local profile/reference continuity. Standard library only; no generation."""
import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(record_path):
    record_path = Path(record_path).expanduser().resolve()
    errors, warnings, checked = [], [], []

    def load(path):
        return json.loads(path.read_text(encoding="utf-8"))

    def resolve(path, base, profile_dir=None):
        candidate = Path(path).expanduser()
        if base == "absolute":
            if not candidate.is_absolute():
                raise ValueError("path_base=absolute requires an absolute path")
            return candidate.resolve()
        if candidate.is_absolute():
            raise ValueError("relative path_base cannot contain an absolute path")
        if base == "record":
            return (record_path.parent / candidate).resolve()
        if base == "profile" and profile_dir is not None:
            return (profile_dir / candidate).resolve()
        raise ValueError("unknown path base: " + str(base))

    def check_file(path, expected_hash, label):
        if not path.is_file():
            errors.append(label + ": file is missing")
            return
        if sha256(path) != expected_hash:
            errors.append(label + ": SHA-256 mismatch")
            return
        checked.append(label)

    try:
        record = load(record_path)
        c = record["character"]
        profile_path = resolve(c["profile_path"], c["path_base"])
        check_file(profile_path, c["profile_sha256"], "profile")
        profile = load(profile_path)
        if (profile["id"], profile["version"]) != (c["profile_id"], c["profile_version"]):
            errors.append("profile ID/version does not match the record")
        profile_refs = {ref["id"]: ref for ref in profile["references"]}
        if len(profile_refs) != len(profile["references"]):
            errors.append("profile reference IDs must be unique")
        selected_ids = [ref["id"] for ref in c["references"]]
        if len(selected_ids) != len(set(selected_ids)):
            errors.append("selected reference IDs must be unique")
        has_primary = False
        for ref in c["references"]:
            path = resolve(ref["path"], ref["path_base"], profile_path.parent)
            check_file(path, ref["sha256"], "reference " + ref["id"])
            if ref["role"] in ("primary_identity", "identity_view", "body"):
                canonical = profile_refs.get(ref["id"])
                if canonical is None:
                    errors.append("identity/body reference is not in this profile: " + ref["id"])
                    continue
                canonical_path = resolve(canonical["path"], "absolute" if Path(canonical["path"]).is_absolute() else "profile", profile_path.parent)
                if canonical_path != path or canonical["sha256"] != ref["sha256"] or canonical["role"] != ref["role"]:
                    errors.append("selected reference differs from the profile: " + ref["id"])
                if not canonical["active"] or canonical["canon_version"] != profile["version"]:
                    errors.append("selected identity/body reference is inactive or from another Canon version: " + ref["id"])
                has_primary |= ref["role"] == "primary_identity"
        ready = profile["status"] == "ready" and has_primary
        if profile["status"] == "ready" and not has_primary:
            errors.append("ready profile requires a selected primary identity reference")
        if profile["status"] == "draft":
            warnings.append("Draft profile: usable for first design, not evidence of a stable existing identity.")

        g = record["generation"]
        qc = record["qc"]
        if record["record_stage"] == "plan" and g["status"] != "not_requested":
            errors.append("plan cannot claim a submitted or generated task")
        if record["record_stage"] == "generated" and g["status"] == "not_requested":
            errors.append("generated record cannot be not_requested")
        if g["status"] == "not_requested":
            if any(value is not None for key, value in g.items() if key != "status"):
                errors.append("not_requested generation fields must be null")
        elif not g["submitted_at"]:
            errors.append("submitted generation requires an actual submission time")
        if g["status"] == "succeeded":
            image = g["image"]
            if not image or not (image["local_path"] or image["url"]):
                errors.append("succeeded generation requires an image path or URL")
            elif image["local_path"]:
                image_path = resolve(image["local_path"], image.get("path_base", "absolute"))
                if image["sha256"]:
                    check_file(image_path, image["sha256"], "generated image")
                elif not image_path.is_file():
                    errors.append("generated image file is missing")
            if not g["completed_at"]:
                errors.append("succeeded generation requires a completion time")
        elif g["image"] is not None:
            errors.append("non-succeeded generation cannot claim an output image")
        if qc["status"] != "not_reviewed":
            if g["status"] != "succeeded" or not qc["reviewed_at"]:
                errors.append("reviewed QC requires a succeeded image and review time")
        elif qc["reviewed_at"] is not None or qc["findings"]:
            errors.append("unreviewed image cannot claim review time or findings")
        weather = record["context"]["weather"]
        if weather["basis"] in ("observed", "forecast"):
            if not all(weather[k] for k in ("source", "retrieved_at")):
                errors.append("observed/forecast weather requires source and retrieval time")
        if weather["basis"] == "forecast" and not weather["valid_at"]:
            errors.append("forecast weather requires a valid time")
        if weather["basis"] in ("unknown", "not_applicable"):
            if any(weather[k] is not None for k in ("valid_at", "temperature_c", "feels_like_c", "precipitation", "wind")):
                errors.append("unknown/not_applicable weather cannot contain invented measurements")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(str(exc))
        ready = False
    return {
        "ok": not errors,
        "ready_for_identity_continuation": ready and not errors,
        "checked_files": checked,
        "warnings": warnings,
        "errors": errors,
        "scope": "Local evidence and state checks only; not a full JSON Schema or visual identity assessment.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", help="Path to one image plan or metadata JSON")
    args = parser.parse_args()
    result = verify(args.record)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["ok"] else 1)
