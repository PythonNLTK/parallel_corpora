# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
# from nltk.corpus import stopwords
from nltk import FreqDist
import time, nltk
# from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer

t1 = time.time()

lmtzr = WordNetLemmatizer()

data_tok = brown.words()

#data_tok = nltk.word_tokenize(data)
data_lower = []
for token in data_tok:
    data_lower.append(token.lower())
    
#data_lemma = [lmtzr.lemmatize(token) for token in data_lower]
    
pos_tagged = nltk.pos_tag(data_lower)

term_freq = []

for i in range(0, len(pos_tagged) - 2):
#     if pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN' and pos_tagged[i+3][1] == 'NN' and pos_tagged[i+4][1] == 'NN':
#         term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
    if pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN' and pos_tagged[i+3][1] == 'NN':
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
    elif pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN' and pos_tagged[i+2][1] == 'NN':
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0]))
    elif pos_tagged[i][1] == 'NN' and pos_tagged[i+1][1] == 'NN':
        term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0]))
                        
fdist = FreqDist(term_freq)

for i in range(0, 50):
    print fdist[i]

print time.time() - t1
    
    
    