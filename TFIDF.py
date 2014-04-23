# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk import FreqDist
import time, nltk, math, operator, codecs
from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()

t1 = time.time()

fdist = FreqDist()

test_set = codecs.open('/home/michi/corpora/testset', 'r', 'utf8')
data = test_set.read()

data_tokenized = nltk.word_tokenize(data)
data_lowercased = [token.lower() for token in data_tokenized]
data_lemmas = [lmtzr.lemmatize(token) for token in data_lowercased]
data_tagged = nltk.pos_tag(data_tokenized)
# tagged_dict = {}
# for entry in data_tagged:
#     tagged_dict[lmtzr.lemmatize(entry[0])] = entry[1]

for token in data_lemmas:
    fdist.inc(token)
    
doc_dic = defaultdict(list)
for fileid in brown.fileids():
    for token in brown.words(fileids=[fileid]):
        if token in doc_dic:
            if not fileid in doc_dic[token]:
                doc_dic[lmtzr.lemmatize(token)].append(fileid)
        else:
            doc_dic[lmtzr.lemmatize(token)] = [fileid]

tfidf = {}
for token in data_lemmas:
    max_value = max(fdist.values())
    tfidf[token] = (fdist[token]/len(fdist)) * (math.log(500 / (1 + len(doc_dic[token]))))
    
for k in tfidf.keys():
    if k in stopwords.words('english') or k in [',', '.', ':', ';', '(', ')', '[', ']', "''", "``"]:
        del tfidf[k]

sorted_tfidf = sorted(tfidf.iteritems(), key=operator.itemgetter(1))

for entry in sorted_tfidf:
    print entry

print time.time() - t1
