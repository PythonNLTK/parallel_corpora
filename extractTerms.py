# -*- coding: utf-8 -*- 
from __future__ import division
import codecs

def readSingleWords():
    
    source = '/home/michi/corpora/tfidf_results.txt'
    singleWordList = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            singleWordList.append(line.split(','))
        
    # [0] = string, [1] = score
    return singleWordList

def readMultiWords():
    
    source = '/home/michi/corpora/pos_results.txt'
    multiWordList = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            multiWordList.append(line.split(','))
            
    # [0] = term, [1] = count
    return multiWordList

if __name__ == '__main__':
    
    print readSingleWords()[-10:]
