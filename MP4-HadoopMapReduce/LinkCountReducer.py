#!/usr/bin/env python3
import sys
from collections import defaultdict

pages = defaultdict(list)


# input comes from STDIN
for line in sys.stdin:
    page_id, source = line.strip().split('\t')
    if len(source.strip()) == 0:
        continue
    else:
        pages[page_id.strip()].append(source.strip())

for key, value in pages.items():
    print('%s\t%s' % (key, len(value)))  