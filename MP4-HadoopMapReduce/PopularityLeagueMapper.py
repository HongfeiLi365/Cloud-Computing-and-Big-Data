#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]

with open(leaguePath) as f:
    lines = f.readlines()
    candidates = [x.strip() for x in lines]

for line in sys.stdin:
    page_id, counts = line.strip().split('\t')

    if page_id.strip() in candidates:
        print('%s\t%s' % ('reduce', counts+', '+page_id))  # pass this output to reducer
