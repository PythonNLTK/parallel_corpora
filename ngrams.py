# -*- coding: utf-8 -*- 
from __future__ import division

import time, nltk
from multiprocessing import Pool
from nltk.corpus import brown

t1 = time.time()

data = brown.words(fileids=['ca01'])

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])
  
ngrams = find_ngrams(data, 5)
tagged = []
for elem in ngrams:
    tagged.append(nltk.pos_tag(elem))

def findCandidates(ngram):
    ngrams = []
    ngrams.append(ngram)
    
    return ngrams

if __name__ == '__main__':
    pool = Pool(processes=8)
    res = pool.map(findCandidates, tagged)
    
    print res
    
print time.time() - t1
