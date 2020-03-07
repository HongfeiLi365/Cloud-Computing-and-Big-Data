#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
import string
import re


def tokenize(line):
    line = line.lower().strip().strip('\n')
    line = re.split(delimiters, line)
    line = filter(None, line)
    line = filter(lambda x: x not in stopwords, line)
    return line


stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    lines = f.readlines()
    stopwords = [x.strip() for x in lines]

with open(delimitersPath) as f:
    lines = f.readlines()
    delimiters = lines[0]

delimiters = " |\t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|_|\*|\/"

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)

words = lines.flatMap(tokenize)

counts = words.map(lambda word: (word, 1))\
    .reduceByKey(lambda a, b: a + b)\
    .sortByKey(ascending=False)

tops = counts.sortBy(ascending=False, keyfunc=lambda a: a[1]).take(10)
tops = sorted(tops)

outputFile = open(sys.argv[4], "w")

# write results to output file. Foramt for each line: (line +"\n")
for (word, count) in tops:
    outputFile.write(word+"\t"+str(count)+"\n")

outputFile.close()
sc.stop()
