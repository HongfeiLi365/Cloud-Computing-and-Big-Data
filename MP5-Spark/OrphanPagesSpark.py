#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

def orphan_mapper(line):
    page_id, targets = line.strip().split(': ')
    targets = targets.strip().split(' ')
    targets = [t.strip() for t in targets]
    targets = filter(lambda x: len(x) > 0, targets)

    to_return = []
    for t in targets:
        to_return.append((t, page_id))
    to_return.append((page_id, 'self'))

    return to_return

def count_links(pair):
    if pair[1] !='self':
        return pair[0], 1
    else:
        return pair[0], 0

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

pairs = lines.flatMap(orphan_mapper)
counts = pairs.map(count_links).reduceByKey(lambda a, b: a + b)
orphans = counts.filter(lambda x: x[1]==0).sortByKey()

    
output = open(sys.argv[2], "w")
#write results to output file. Foramt for each line: (line+"\n")
for (page, count) in orphans.collect():
    output.write(page+"\n")

output.close()
sc.stop()

