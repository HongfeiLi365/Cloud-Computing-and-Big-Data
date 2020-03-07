#!/usr/bin/env python3
import sys

for line in sys.stdin:
    page, count = line.strip().split('\t')
    if len(count.strip())>0:
        print('%s\t%s' % (0, count+', '+page))  # pass this output to reducer
