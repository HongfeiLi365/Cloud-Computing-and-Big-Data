#!/usr/bin/env python3
import sys
import math

nums=[]
for line in sys.stdin:
    key, count = line.strip().split('\t')
    if key == 'count':
        nums.append(int(count))

stat={}
stat['Min'] = min(nums)
stat['Max'] = max(nums)
stat['Sum'] = sum(nums)
stat['Mean'] = stat['Sum'] // len(nums)
s = 0
for n in nums:
    s = s + (n - stat['Mean'])**2
stat['Var'] = s // len(nums)

for st in ['Mean', 'Sum', 'Min', 'Max', 'Var']:
    print('%s\t%s' % (st,stat[st])) # print as final output

