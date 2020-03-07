#!/usr/bin/env python3
import sys


for line in sys.stdin:
    page_id, targets = line.strip().split(': ')
    targets = targets.strip().split(' ')
    targets = [t.strip() for t in targets]
    targets = filter(lambda x: len(x) > 0, targets)

    for t in targets:
        print('%s\t%s' % (t, page_id))  

