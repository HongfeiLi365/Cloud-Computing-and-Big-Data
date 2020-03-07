#!/usr/bin/env python3
import sys
from collections import defaultdict

pages = defaultdict(list)

for line in sys.stdin:
    page_id, source = line.strip().split('\t')
    if len(source.strip()) == 0:
        continue
    else:
        pages[page_id.strip()].append(source.strip())


for key, value in pages.items():
    if len(value) == 1 and value[0] == 'self':
        print(key)  # print as final output
