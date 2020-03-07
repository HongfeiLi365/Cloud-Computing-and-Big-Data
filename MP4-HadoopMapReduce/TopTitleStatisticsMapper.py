#!/usr/bin/env python3
import sys


for line in sys.stdin:
    word, value = line.strip().split('\t')
    print('%s\t%s' % ('count', value))  # pass this output to reducer
