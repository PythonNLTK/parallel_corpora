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

#data = "A computer is a general purpose device that can be programmed to carry out a set of arithmetic or logical operations automatically. Since a sequence of operations can be readily changed, the computer can solve more than one kind of problem. Conventionally, a computer consists of at least one processing element, typically a central processing unit (CPU), and some form of memory. The processing element carries out arithmetic and logic operations, and a sequencing and control unit can change the order of operations in response to stored information. Peripheral devices allow information to be retrieved from an external source, and the result of operations saved and retrieved. In World War II, mechanical analog computers were used for specialized military applications. During this time the first electronic digital computers were developed. Originally they were the size of a large room, consuming as much power as several hundred modern personal computers (PCs). Modern computers based on integrated circuits are millions to billions of times more capable than the early machines, and occupy a fraction of the space.[2] Simple computers are small enough to fit into mobile devices, and mobile computers can be powered by small batteries. Personal computers in their various forms are icons of the Information Age and are what most people think of as 'computers.' However, the embedded computers found in many devices from MP3 players to fighter aircraft and from toys to industrial robots are the most numerous."

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
