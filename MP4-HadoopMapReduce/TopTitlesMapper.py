#!/usr/bin/env python3
import sys


for line in sys.stdin:
    word, value = line.strip().split('\t')
    print('%s\t%s' % (0, value+', '+word))  # pass this output to reducer
