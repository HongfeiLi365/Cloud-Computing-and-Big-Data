#!/usr/bin/env python3
import sys
from collections import defaultdict

freq = defaultdict(int)
inv_freq = defaultdict(list)
# input comes from STDIN
for line in sys.stdin:
    _, count_word = line.strip().split('\t')
    try:
        count, word = count_word.strip().split(', ')
    except:
        continue
    freq[word] = freq[word] + int(count)
    inv_freq[int(count)].append(word)

for k in inv_freq.keys():
    inv_freq[k] = sorted(inv_freq[k])
    
ret = sorted(inv_freq.items(), reverse=True)
ret = list(zip(*ret))[1]
ret = [x for s in ret for x in s]

for word in sorted(ret[:10]):
    print('%s\t%s' % (word, freq[word])) 

    