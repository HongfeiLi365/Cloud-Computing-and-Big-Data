#!/usr/bin/env python3
import sys
from collections import defaultdict

inv_freq = defaultdict(list)
for line in sys.stdin:
    try:
        key, count_page = line.strip().split('\t')
    except:
        continue
    if key.strip() != 'reduce':
        continue
    else:
        count, page = count_page.split(', ')
        inv_freq[int(count)].append(page)


for k in inv_freq.keys():
    inv_freq[k] = sorted(inv_freq[k], reverse=True)

ret = sorted(inv_freq.items())
ranks = []
rank=0
for i in range(len(ret)):
    for p in ret[i][1]:
        ranks.append((p, rank))
    rank = rank + len(ret[i][1])

ranks = sorted(ranks, reverse=True)
for p, r in ranks:
    print('%s\t%s' % (p,r))
