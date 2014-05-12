# -*- coding: utf-8 -*- 
from __future__ import division
import nltk, codecs

def tokenize(rawData):
    
    return nltk.word_tokenize(rawData)
    
def tag(tokenizedData):
    
    return nltk.pos_tag(tokenizedData)
    
def writeToFile(taggedData):
    
    outputFile = '/home/michi/corpora/testset_tagged'
    with codecs.open(outputFile, 'w', encoding='utf-8') as myFile:
        for tup in taggedData:
            myFile.write(tup[0] + ',' + tup[1] + '\n')
    
if __name__ == '__main__':
    
    inputFile = '/home/michi/corpora/testset'

    handle = codecs.open(inputFile, 'r', encoding='utf-8')
    raw = handle.read()
    handle.close()
    tokenized = tokenize(raw)
    tagged = tag(tokenized)
    writeToFile(tagged)
    
    