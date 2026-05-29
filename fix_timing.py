# -*- coding: utf-8 -*-
"""Wrap chat IIFE in DOMContentLoaded to fix timing issue"""
import re

with open(r"F:\ARCHILABS_AI\gis-landing\index.html", encoding="utf-8") as f:
    h = f.read()

# Find the last (function(){ ... })(); block
pattern = r'\(function\(\)\{(.*?)\}\)\(\);'
matches = list(re.finditer(pattern, h, re.DOTALL))
print(f"Found {len(matches)} IIFE blocks")

if matches:
    m = matches[-1]
    inner = m.group(1)
    replacement = 'document.addEventListener("DOMContentLoaded", function(){' + inner + '});'
    h = h[:m.start()] + replacement + h[m.end():]
    print("Wrapped in DOMContentLoaded ✅")
else:
    print("No IIFE found!")

with open(r"F:\ARCHILABS_AI\gis-landing\index.html", "w", encoding="utf-8") as f:
    f.write(h)
print("Saved!")
