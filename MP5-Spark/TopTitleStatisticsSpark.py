#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1],1)

counts = lines.map(lambda line: int(line.strip().split('\t')[1].strip()))

mean_ = int(counts.mean())
sum_ = counts.sum()
min_ = counts.min()
max_ = counts.max()
var_ = int(counts.variance())


outputFile = open(sys.argv[2],"w")
'''
write your output here
write results to output file. Format
'''
outputFile.write('Mean\t%s\n' % mean_)
outputFile.write('Sum\t%s\n' % sum_)
outputFile.write('Min\t%s\n' % min_)
outputFile.write('Max\t%s\n' % max_)
outputFile.write('Var\t%s\n' % var_)

outputFile.close()
sc.stop()

