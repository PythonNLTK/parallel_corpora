# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
from nltk.corpus import stopwords
import time, nltk, math, operator, re
from nltk.stem.wordnet import WordNetLemmatizer
from multiprocessing import Pool

lmtzr = WordNetLemmatizer()

def prepareData(data):
    #data_tokenized = nltk.word_tokenize(data)
    data_lowercased = [token.lower() for token in data]
    bigrams = nltk.bigrams(data_lowercased)
    #bigramsFreq = nltk.FreqDist(bigrams)

    return bigrams

def calcChiSqr(bg):
    
    bigram_dic = {}
    
    # w1, w2: sum11 / w1: sum12 / w2: sum21 / none: sum22
    
    sum11, sum12, sum21, sum22 = 0, 0, 0, 0
    
    #for bg in bigrams:
    for bigram in bigrams:
        if bg[0] == bigram[0] and bg[1] == bigram[1]:
            sum11 += 1
        elif bg[0] != bigram[0] and bg[1] == bigram[1]:
            sum12 += 1
        elif bg[0] == bigram[0] and bg[1] != bigram[1]:
            sum21 += 1
        elif bg[0] != bigram[0] and bg[1] != bigram[1]:
            sum22 += 1
                
    bigram_dic[bg] = ( len(data) * math.pow(sum11*sum22 - sum12*sum21, 2) ) / ( (sum11+sum12) * (sum11+sum21) * (sum12+sum22) * (sum21+sum22) )
        
    return bigram_dic
        
def filterResults(bigram_dic):
    
    sorted_bigram_chisqr = sorted(bigram_dic.iteritems(), key=operator.itemgetter(1))

    for entry in sorted_bigram_chisqr:
        if not entry[0][0] in stopwords.words('english') and not entry[0][1] in stopwords.words('english') \
            and nonPunct.match(entry[0][0]) and nonPunct.match(entry[0][1]):
            print entry

if __name__ == '__main__':
    
    data = brown.words(fileids=['ca01', 'ca02', 'ca03', 'ca04', 'ca05', 'ca06', 'ca07', 'ca08', 'ca09', 'ca10', 'ca11', 'ca12', 'ca13', 'ca14', 'ca15', 'ca16', 'ca17', 'ca18', 'ca19', 'ca20']) 
    nonPunct = re.compile('[A-Za-z0-9]')
        
    t1 = time.time()
    
    bigrams = prepareData(data)
    pool = Pool(processes=2)
    result = pool.map(calcChiSqr, bigrams)
    #bigram_dic = calcChiSqr(bigrams)
    filterResults(result[0])
        
    print time.time() - t1
    