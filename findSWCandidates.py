# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
from nltk import FreqDist
import time, math, codecs, operator
from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

lmtzr = WordNetLemmatizer()

def readStopWords():
    
    sourceFile = '/home/michi/corpora/stopwords.txt'
    with codecs.open(sourceFile, 'r', encoding='utf-8') as myFile:
        stopwords = myFile.read().split()
        
    return stopwords

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
    for entry in data_lemmas:
        try:
            if not entry[0] in tfidf:
                tfidf[lmtzr.lemmatize(entry[0])] = [(fdist[entry]/tokCount) * (math.log(500 / (1 + len(doc_dic[entry[0]])))), entry[1]]
            else:
                tfidf[lmtzr.lemmatize(entry[0])].extend([(fdist[entry]/tokCount) * (math.log(500 / (1 + len(doc_dic[entry[0]])))), entry[1]])
        except:
            continue
            
    for k,v in tfidf.items():
        if len(v) > 2:
            temp = 0
            for b in v:
                if type(b) == float:
                    temp += b
            tfidf[k] = [temp, v[1]]     
        
    return tfidf
        
def filterResults(tfidf):
    for k,v in tfidf.items():
        if not (not k in stopwords and k.isalpha() and len(k) > 1 and (v[1] == 'NN' or v[1] == 'NNS')):
            del tfidf[k]
    
    return tfidf
        
def writeToFile(sorted_output):
    with codecs.open('/home/michi/corpora/tfidf_results.txt', 'w', encoding='utf-8') as outputFile:
        for entry in sorted_output:
            outputFile.write(entry[0] + ',' + str(entry[1][0]) + '\n')

if __name__ == '__main__':
    
    t1 = time.time()
    
    stopwords = readStopWords()
    data_lemmas = prepareData()
    fdist = calcFreq(data_lemmas)
    doc_dic = calcDF()
    
    tfidf_scores = calcTFIDF(data_lemmas)
    
    tfidf_filtered = filterResults(tfidf_scores)
    sorted_tfidf = sorted(tfidf_scores.iteritems(), key=operator.itemgetter(1), reverse=True)
    writeToFile(sorted_tfidf)
    
    print time.time() - t1
