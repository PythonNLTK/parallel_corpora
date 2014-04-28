# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
# from nltk.corpus import stopwords
from nltk import FreqDist
import time, nltk, codecs
# from collections import defaultdict

t1 = time.time()

#data_tok = nltk.word_tokenize(data)
test_set = codecs.open('/home/michi/corpora/testset', 'r', 'utf8')
data = test_set.read()
data_tok = nltk.word_tokenize(data)
#data_tok = brown.words(fileids=['ca01', 'ca02', 'cd01', 'cd02', 'ch01', 'ch02'])
#data_lower = [token.lower() for token in data_tok]
    
pos_tagged = nltk.pos_tag(data_tok)

term_freq = []

rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in range(0, len(pos_tagged) - 5):
    
#     if (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS') and (pos_tagged[i+4][1] == 'NN' or pos_tagged[i+4][1] == 'NNS'):
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
#         rule1 += 1
#         
#     elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and pos_tagged[i+2][1] == 'DT' and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS') and (pos_tagged[i+4][1] == 'NN' and pos_tagged[i+4][1] == 'NNS'):
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
#         rule2 += 1
#         
    if (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and pos_tagged[i+2][1] == 'DT' and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
        rule3 += 1
         
    elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and pos_tagged[i+2][1] == 'IN' and pos_tagged[i+3][1] == 'DT' and (pos_tagged[i+4][1] == 'NN' or pos_tagged[i+4][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
        rule4 += 1
      
    elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
        rule5 += 1
        
    elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
        rule6 += 1
            
#     elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#         rule7 += 1
#         
#     elif pos_tagged[i][1] == 'JJ' and pos_tagged[i+1][1] == 'JJ' and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#         rule8 += 1
#         
    elif pos_tagged[i][1] == 'JJ' and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and pos_tagged[i+2][1] == 'IN'  and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
        rule9 += 1
        
    elif pos_tagged[i][1] == 'JJ' and pos_tagged[i+1][1] == 'JJ' and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
        rule10 += 1

    elif pos_tagged[i][1] == 'JJ' and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
        rule11 += 1
        
    elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
        rule13 += 1
        
    elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and ( pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS'):
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0]))
        rule12 += 1
                        
fdist = FreqDist(term_freq)

for i in range(0, 100):
    print fdist.items()[i]

print rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13

print time.time() - t1
    
    
    