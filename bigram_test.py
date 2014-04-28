# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import stopwords
import time, nltk, math, operator, re, codecs
from nltk.collocations import *

def prepareData(raw):
    data_tokenized = nltk.word_tokenize(raw)
    data_lowercased = [token.lower() for token in data_tokenized]
    
    return data_lowercased

def calcScores(data):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(data)

    return finder.nbest(bigram_measures.likelihood_ratio, 1000)

def filterResults(unfiltered):
    for entry in unfiltered:
        if not entry[0] in stopwords.words('english') and not entry[1] in stopwords.words('english') and entry[0].isalpha() and entry[1].isalpha():
            print entry
    
if __name__ == '__main__':
    
    source = codecs.open('/home/michi/corpora/testset', 'r', 'utf8').read()
    nonPunct = re.compile('[A-Za-z0-9]')
    
    t1 = time.time()
    
    text = prepareData(source)
    calc = calcScores(text)
    filterResults(calc)
        
    print time.time() - t1