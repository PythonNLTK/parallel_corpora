# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk import FreqDist
import time, nltk, math, operator, codecs, re
from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()

def prepareData():
        
    test_set = codecs.open('/home/michi/corpora/testset', 'r', 'utf8')
    data = test_set.read()
    
    data_tokenized = nltk.word_tokenize(data)
    data_lowercased = [token.lower() for token in data_tokenized]
    data_lemmas = [lmtzr.lemmatize(token) for token in data_lowercased]

    #data_tagged = nltk.pos_tag(data_tokenized)
    # tagged_dict = {}
    # for entry in data_tagged:
    #     tagged_dict[lmtzr.lemmatize(entry[0])] = entry[1]

    return data_lemmas

def calcFreq(data_lemmas):
    fdist = FreqDist()
    for token in data_lemmas:
        fdist.inc(token)
        
    return fdist

def calcDF():
    
    doc_dic = defaultdict(set)
    for fileid in brown.fileids():
        for token in brown.words(fileids=[fileid]):
            doc_dic[lmtzr.lemmatize(token)].add(fileid)
            
    return doc_dic


def calcTFIDF(data_lemmas):
    tfidf = {}
    tokCount = len(fdist)
    for token in set(data_lemmas):
        tfidf[token] = (fdist[token]/tokCount) * (math.log(500 / (1 + len(doc_dic[token]))))
        
    return tfidf
        
def filterResults(tfidf):
    nonPunct = re.compile('[A-Za-z]')
    for k in tfidf.keys():
        if k in stopwords.words('english') or not nonPunct.match(k):
            del tfidf[k]
            
    return tfidf

# def output(sorted):
#     for entry in sorted:
#         print entry
        
def writeToFile(sorted_output):
    with codecs.open('/home/michi/corpora/tfidf.txt', 'w', encoding='utf-8') as outputFile:
        for entry in sorted_output:
            outputFile.write(entry[0] + ',' + str(entry[1]) + '\n')


if __name__ == '__main__':
    
    t1 = time.time()
    
    data_lemmas = prepareData()
    fdist = calcFreq(data_lemmas)
    doc_dic = calcDF()
    
    tfidf = calcTFIDF(data_lemmas)
    
    tfidf_filtered = filterResults(tfidf)
    sorted_tfidf = sorted(tfidf_filtered.iteritems(), key=operator.itemgetter(1))
    writeToFile(sorted_tfidf)
    
    print time.time() - t1
