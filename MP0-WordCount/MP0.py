import random 
import os
import string
import sys
import re
from collections import defaultdict


stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#delimiters = " \t,;.?!-:@[](){}_*/"
delimiters = " |\t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|_|\*|\/|"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    
    # begin my code
    lines = sys.stdin.readlines()
#    
#    f = open("input.txt","r")
#    lines = f.readlines()
#    f.close()
#    
    frequencies = defaultdict(int)
    for i in indexes:
        line = lines[i]
        line = line.lower().strip().strip('\n')
        line = re.split(delimiters, line)
        line = filter(None, line)
        for word in line:
            if word not in stopWordsList:
                frequencies[word] = frequencies[word] + 1
    
    
    inv_freq = defaultdict(list)
    for k, v in frequencies.iteritems():
        inv_freq[v].append(k)
        
    for k in inv_freq.keys():
        inv_freq[k] = sorted(inv_freq[k])
        
    
    
    
    ret = sorted(inv_freq.iteritems(), reverse=True)
    ret = zip(*ret)[1]
    ret = [x for s in ret for x in s]
    # end my code
    
    for word in ret[:20]:
        print word

process(sys.argv[1])
