# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
# from nltk.corpus import stopwords
from nltk import FreqDist
import time, nltk
# from collections import defaultdict

t1 = time.time()

#data_tok = nltk.word_tokenize(data)
data_tok = brown.words()
#data_tok = brown.words(fileids=['ca01', 'ca02', 'cd01', 'cd02', 'ch01', 'ch02'])
#data_lower = [token.lower() for token in data_tok]
    
pos_tagged = nltk.pos_tag(data_tok)

term_freq = []

for i in range(0, len(pos_tagged) - 2):
#     if pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN' and pos_tagged[i+3][1] == 'NN' and pos_tagged[i+4][1] == 'NN':
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
    if pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN' and pos_tagged[i+3][1] == 'NN':
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#     elif pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN':
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
    elif pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN':
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0]))
#     elif pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'IN' and pos_tagged[i+2][1] == 'NN':
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
    elif (pos_tagged[i][1] == 'JJ' or pos_tagged[i][1] == 'NN') and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN':
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
                        
fdist = FreqDist(term_freq)

for i in range(0, 20):
    print fdist.items()[i]

print time.time() - t1
    
    
    