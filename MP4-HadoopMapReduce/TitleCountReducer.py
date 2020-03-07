#!/usr/bin/env python3
from operator import itemgetter
import sys


frequencies = {}
# input comes from STDIN
for line in sys.stdin:
    word, value = line.split('\t')
    if word in frequencies:
        frequencies[word] = frequencies[word] + 1
    else:
        frequencies[word] = 1

for key in frequencies:
    print('%s\t%s' % (key, frequencies[key])) # print as final output