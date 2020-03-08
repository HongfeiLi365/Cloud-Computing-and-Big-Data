#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

def link_count_mapper(line):
    page_id, targets = line.strip().split(': ')
    targets = targets.strip().split(' ')
    targets = [t.strip() for t in targets]
    targets = filter(lambda x: len(x) > 0, targets)

    to_return = [(t, 1) for t in targets if t in candidates]
    return to_return

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

leagueIds = sc.textFile(sys.argv[2], 1)
candidates = leagueIds.map(lambda x: x.strip()).collect()


counts = lines.flatMap(link_count_mapper).reduceByKey(lambda a, b: a + b)
counts = counts.sortByKey()
tops = counts.sortBy(keyfunc=lambda a: a[1]).collect()

ranks = [(tops[0][0],0)]

for i in range(1, len(tops)):
    j = i - 1
    while j >=0:
        if tops[j][1] == tops[i][1]:
            j = j - 1
        else:
            break
    ranks.append((tops[i][0], j+1))
    
ranks = sorted(ranks)

output = open(sys.argv[3], "w")
#write results to output file. Foramt for each line: (key + \t + value +"\n")
for (page, rank) in ranks:
    output.write(page+"\t"+str(rank)+"\n")
output.close()
sc.stop()

