#!/usr/bin/env python3
"""Restore historical case-sensitive 2025B URLs in the Linux deployment."""
from pathlib import Path
import html
import shutil
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public')
# Never write case-only duplicate names on case-insensitive local filesystems.
old = root / 'courses' / '2025B'
new = root / 'courses' / '2025b'
if old.exists() and old.samefile(new):
    print('Case-insensitive filesystem: legacy uppercase routes resolve locally.')
    sys.exit(0)
for source, target in [(new, old), (new/'ace', old/'ACE')]:
    target.mkdir(parents=True, exist_ok=True)
    relative = '../2025b/' if source == new else '../../2025b/ace/'
    dest = html.escape(relative, quote=True)
    (target/'index.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Page moved</title><meta name="robots" content="noindex"><link rel="canonical" href="{dest}"><meta http-equiv="refresh" content="0;url={dest}"></head><body><p><a href="{dest}">Continue to the current course page</a>.</p></body></html>', encoding='utf-8')
    for pdf in source.glob('*.pdf'):
        shutil.copy2(pdf, target / pdf.name)
# Accept the historic period casing with either version of the course casing.
for source, target in [(new/'ace', old/'ace'), (new/'ace', new/'ACE')]:
    target.mkdir(parents=True, exist_ok=True)
    relative = '../../2025b/ace/' if target.parent == old else '../ace/'
    (target/'index.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Page moved</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={relative}"></head><body><a href="{relative}">Continue to the course page</a></body></html>', encoding='utf-8')
    for pdf in source.glob('*.pdf'): shutil.copy2(pdf, target / pdf.name)
