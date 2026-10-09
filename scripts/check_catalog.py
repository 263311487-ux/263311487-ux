#!/usr/bin/env python3
import re
from collections import Counter

ROLES={'product','research','demo','profile','placeholder','fork'}
STATES={'open','closed','merged'}
NAME=re.compile(r'^[A-Za-z0-9_.-]+$')

def validate(doc):
    rows=doc.get('repositories',[])
    if doc.get('schema_version') != 1 or not isinstance(rows,list): raise ValueError('invalid catalog')
    names=[]
    for row in rows:
        name=row.get('name')
        if not isinstance(name,str) or not NAME.fullmatch(name) or name in names: raise ValueError('invalid/duplicate name')
        names.append(name)
        role=row.get('lifecycle')
        if role not in ROLES: raise ValueError('invalid lifecycle')
        parent=row.get('upstream')
        if role=='fork' and (not isinstance(parent,str) or not re.fullmatch(r'[^/\s]+/[^/\s]+',parent)): raise ValueError('fork parent required')
        if role!='fork' and parent is not None: raise ValueError('nonfork upstream')
        for pr in row.get('pull_requests',[]):
            if type(pr.get('number')) is not int or pr['number']<1 or pr.get('state') not in STATES: raise ValueError('invalid pull request')
            if role!='fork' or pr.get('url') != f'https://github.com/{parent}/pull/{pr["number"]}': raise ValueError('pull request does not belong to upstream')
    if 'pr_search' in doc:
        prs=[p for r in rows for p in r.get('pull_requests',[])]
        excluded=doc.get('excluded_pull_requests',[])
        for p in excluded:
            if p.get('state') not in STATES or not p.get('reason') or not p.get('url','').startswith('https://github.com/'):
                raise ValueError('invalid excluded pull request')
        all_prs=prs+excluded
        if len({p['url'] for p in all_prs})!=len(all_prs): raise ValueError('duplicate pull request')
        search=doc['pr_search']
        if search.get('total_count') != len(all_prs): raise ValueError('search total does not reconcile')
        counts=Counter(p['state'] for p in all_prs)
        if any(search.get('counts',{}).get(s,0)!=counts[s] for s in STATES): raise ValueError('search states do not reconcile')
    return {'total':len(rows),'forks':sum(r['lifecycle']=='fork' for r in rows)}

if __name__=='__main__':
    import argparse,json
    p=argparse.ArgumentParser();p.add_argument('file');a=p.parse_args()
    with open(a.file,encoding='utf-8') as f:doc=json.load(f)
    print(json.dumps(validate(doc),ensure_ascii=False))
