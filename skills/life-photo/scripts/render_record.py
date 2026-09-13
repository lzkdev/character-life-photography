#!/usr/bin/env python3
"""Render a human-readable Markdown view of one record; never changes its JSON."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import quote


def value_text(value):
    if value is None:
        return '未记录'
    if isinstance(value, bool):
        return '是' if value else '否'
    return str(value)


def tree(value, indent=0):
    if isinstance(value, dict):
        lines=[]
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                lines.append('  '*indent+'- '+str(key)+'：')
                lines.extend(tree(item, indent+1))
            else:
                lines.append('  '*indent+'- '+str(key)+'：'+value_text(item))
        return lines
    if isinstance(value, list):
        return [line for item in value for line in tree(item, indent)] or ['  '*indent+'- 无']
    return ['  '*indent+'- '+value_text(value)]


def render(record_path, output_path):
    r=json.loads(record_path.read_text(encoding='utf-8'))
    generation=r['generation']
    creation=r.get('creation')
    lines=['# 创作记录 · '+r['shot_id'], '',
           '此阅读版来自 ['+record_path.name+']('+quote(os.path.relpath(record_path, output_path.parent), safe='/')+')。', '',
           '**生成状态：'+generation['status']+'；成图检查：'+r['qc']['status']+'。**', '']
    img=generation.get('image') or {}
    if generation['status']=='succeeded' and img.get('local_path'):
        path=Path(img['local_path']).expanduser()
        base=img.get('path_base','absolute')
        if base=='record':
            if path.is_absolute():
                raise ValueError('path_base=record requires a relative image path.')
            path=record_path.parent/path
        elif base=='absolute':
            if not path.is_absolute():
                raise ValueError('A legacy/absolute image path must be absolute.')
        else:
            raise ValueError('Unknown image path base: '+str(base))
        path=path.resolve()
        if not path.is_file():
            raise FileNotFoundError('Referenced image is missing: '+str(path))
        link=quote(os.path.relpath(path, output_path.parent),safe='/')
        lines.extend(['![实际成图]('+link+')',''])
    elif generation['status']=='succeeded' and img.get('url'):
        lines.extend(['图片结果地址：'+img['url'],''])
    if creation:
        lines.extend(['## 创作类型','',creation['type_id']+' · '+creation['type_version'],''])
        if creation['spec']:
            lines.extend(tree(creation['spec'])+[''])
    else:
        lines.extend(['创作类型：旧记录未显式记录；保留原 JSON。',''])
    c=r['character']
    lines.extend(['## 人物依据','', '- 人物：'+c['profile_id'], '- 档案版本：'+c['profile_version'],
                  '- 参考图：'+('、'.join(x['id'] for x in c['references']) or '未选定'), ''])
    sections=[('本次情境',r['context']),('动作与动机',r['event']),('服装与外观',r['appearance']),
              ('镜头互动',r.get('interaction')),('摄影表达',r['photography']),('实际成图检查',r['qc'])]
    for title, value in sections:
        if value is not None:
            lines.extend(['## '+title,'']+tree(value)+[''])
    for title,key in [('完整提示词','standalone'),('本次避免项','negative')]:
        text=r['prompts'].get(key) or ''
        fence='`'*max(3, max((len(x) for x in text.split() if x and set(x)=={'`'}), default=0)+1)
        while fence in text:
            fence+='`'
        lines.extend(['## '+title,'',fence+'text',text,fence,''])
    lines.extend(['生成模型：'+value_text(generation.get('model'))+'；实际尺寸：'+value_text(img.get('width_px'))+' × '+value_text(img.get('height_px'))+'。',''])
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record')
    parser.add_argument('--output')
    parser.add_argument('--replace',action='store_true',help='Refresh a reviewed, reproducible Markdown view.')
    args=parser.parse_args()
    source=Path(args.record).expanduser().resolve()
    output=Path(args.output).expanduser().resolve() if args.output else source.with_suffix('.md')
    if output==source:
        parser.error('Output cannot replace the JSON source.')
    text=render(source,output)
    with output.open('w' if args.replace else 'x',encoding='utf-8') as f:
        f.write(text)
    print(str(output))


if __name__=='__main__':
    main()
