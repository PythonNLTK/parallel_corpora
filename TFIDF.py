# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk import FreqDist
import time, math, codecs, operator
from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()

def readTaggedData():
    
    inputFile = '/home/michi/corpora/testset_tagged'
    taggedData = []
    with codecs.open(inputFile, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            taggedData.append((line.split(',')[0], line.split(',')[1].split('\n')[0]))
            
    return taggedData

def prepareData():

    data_tagged = readTaggedData()
    data_lowercased = []
    for token in data_tagged:
        data_lowercased.append((token[0].lower(), token[1]))

    return data_lowercased

def calcFreq(data_lemmas):
    fdist = FreqDist()
    for token in data_lemmas:
        fdist.inc(token)
        
    return fdist

def calcDF():
    
    doc_dic = defaultdict(set)
    for fileid in brown.fileids():
        for token in brown.words(fileids=[fileid]):
            doc_dic[token].add(fileid)
            
    return doc_dic


def calcTFIDF(data_lemmas):
    tfidf = {}
    tokCount = len(fdist)
    for token in set(data_lemmas):
        if lmtzr.lemmatize(token[0]) in tfidf:
            tfidf[(lmtzr.lemmatize(token[0]), token[1])] += (fdist[token]/tokCount) * (math.log(500 / (1 + len(doc_dic[token[0]]))))
        else:
            tfidf[(lmtzr.lemmatize(token[0]), token[1])] = (fdist[token]/tokCount) * (math.log(500 / (1 + len(doc_dic[token[0]]))))
        
        
    return tfidf
        
def filterResults(tfidf):
    for k in tfidf.keys():
        if not (not k[0] in stopwords.words('english') and k[0].isalpha() and len(k[0]) > 1 and (k[1] == 'NN' or k[1] == 'NNS')):
            del tfidf[k]
    
    return tfidf
        
def writeToFile(sorted_output):
    with codecs.open('/home/michi/corpora/tfidf_results.txt', 'w', encoding='utf-8') as outputFile:
        for entry in sorted_output:
            outputFile.write(entry[0][0] + ',' + str(entry[1]) + '\n')

if __name__ == '__main__':
    
    t1 = time.time()
    
    data_lemmas = prepareData()
    fdist = calcFreq(data_lemmas)
    doc_dic = calcDF()
    
    tfidf_scores = calcTFIDF(data_lemmas)
    
    tfidf_filtered = filterResults(tfidf_scores)
    sorted_tfidf = sorted(tfidf_filtered.iteritems(), key=operator.itemgetter(1), reverse=True)
    writeToFile(sorted_tfidf)
    
    print time.time() - t1
