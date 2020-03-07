#!/usr/bin/env python3

import sys
import string
import re


stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

# stopWordsPath = 'stopwords.txt'
# delimitersPath = 'delimiters.txt'
# f = open("dataset/titles/titles-a","r", encoding='utf-8')
# inputs = f.readlines()[:100]
# f.close()


with open(stopWordsPath) as f:
    lines = f.readlines()
    stopwords = [x.strip() for x in lines]

with open(delimitersPath) as f:
    lines = f.readlines()
    delimiters = lines[0]

delimiters = " |\t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|_|\*|\/"

for line in sys.stdin:
#for line in inputs:
    line = line.lower().strip().strip('\n')
    line = re.split(delimiters, line)
    line = filter(None, line)
    for word in line:
        if word not in stopwords:
            print('%s\t%s' % (word, 1))  # pass this output to reducer
