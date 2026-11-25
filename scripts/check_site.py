#!/usr/bin/env python3
"""Check generated local links, source assets, core pages and HTML metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote, urljoin
import hashlib
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public').resolve()
repo = Path(__file__).resolve().parents[1]
base = 'https://juanvillacres.github.io'
required = ['index.html','research/index.html','papers/index.html','publications/index.html','projects/index.html','courses/index.html','teaching/index.html','courses/2025b/ace/index.html','courses/2026a/ace/index.html','courses/2026b/ace/index.html','courses/2026b/controlinteligente/index.html','posts/index.html','news/index.html','experience/index.html','contact/index.html','404.html','sitemap.xml','robots.txt']
errors = [f'Missing expected route: {p}' for p in required if not (root/p).is_file()]
if (root/'archive').exists(): errors.append('Retired archive route must not be generated')
class Parser(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.links=[]; self.ids=set(); self.title=False; self.description=False; self.main=False; self.h1=0; self.redirect=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'title': self.title=True
        if tag == 'main': self.main=True
        if tag == 'h1': self.h1+=1
        if tag == 'meta' and a.get('name')=='description' and a.get('content'): self.description=True
        if tag == 'meta' and a.get('http-equiv','').lower()=='refresh': self.redirect=True
        if tag in ('a','link') and a.get('href'): self.links.append(a['href'])
        if tag in ('img','script','source') and a.get('src'): self.links.append(a['src'])
        if tag == 'img' and 'alt' not in a: errors.append('Image missing alt attribute')

pages={}
for path in root.rglob('*.html'):
    p=Parser();p.feed(path.read_text(encoding='utf-8'));pages[path]=p
    if not p.redirect and (not p.title or not p.description or not p.main or p.h1!=1): errors.append(f'Missing title, description, main or unique h1: {path.relative_to(root)}')
for path,p in pages.items():
    relative=path.relative_to(root).as_posix(); current=base+'/'+(relative[:-10] if relative.endswith('index.html') else relative)
    for link in p.links:
        u=urlsplit(urljoin(current,link))
        if u.scheme not in ('http','https') or u.netloc!=urlsplit(base).netloc: continue
        target=root/unquote(u.path).lstrip('/')
        if target.is_dir():target=target/'index.html'
        if not target.is_file(): errors.append(f'{relative}: unresolved link {link}');continue
        if u.fragment and target in pages and not pages[target].redirect and unquote(u.fragment) not in pages[target].ids: errors.append(f'{relative}: unresolved fragment {link}')
for pdf in (repo/'static'/'courses').rglob('*.pdf'):
    target=root/pdf.relative_to(repo/'static')
    if not target.is_file() or hashlib.sha256(pdf.read_bytes()).digest()!=hashlib.sha256(target.read_bytes()).digest():errors.append(f'PDF missing or changed: {pdf.name}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'Validated {len(pages)} HTML pages, required routes, local links and teaching PDFs.')
