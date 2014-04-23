# -*- coding: utf-8 -*- 
from __future__ import division

from nltk.corpus import brown
from nltk.corpus import stopwords
import time, nltk, math, operator, re
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()

t1 = time.time()

# data = """A computer is a general purpose device that can be programmed to carry out a set of arithmetic or 
# logical operations automatically. Since a sequence of operations can be readily changed, the computer can solve 
# more than one kind of problem. Conventionally, a computer consists of at least one processing element, typically a 
# central processing unit (CPU), and some form of memory. The processing element carries out arithmetic and logic operations, 
# and a sequencing and control unit can change the order of operations in response to stored information. Peripheral devices 
# allow information to be retrieved from an external source, and the result of operations saved and retrieved. In World War II, 
# mechanical analog computers were used for specialized military applications. During this time the first electronic digital 
# computers were developed. Originally they were the size of a large room, consuming as much power as several hundred modern 
# personal computers (PCs). Modern computers based on integrated circuits are millions to billions of times more capable than 
# the early machines, and occupy a fraction of the space.[2] Simple computers are small enough to fit into mobile devices, and 
# mobile computers can be powered by small batteries. Personal computers in their various forms are icons of the Information Age 
# and are what most people think of as 'computers.' However, the embedded computers found in many devices from MP3 players to 
# fighter aircraft and from toys to industrial robots are the most numerous."""

source = []
data = ''
# for fileid in brown.fileids():
#     source.append(brown.words(fileids=[fileid]))
#    
# for text in source:
#     data += ' '.join(text)

# for fileid in ['ca01', 'ca02', 'ca03', 'ca04', 'ca05', 'ca06', 'ca07', 'ca08', 'ca09', 
#                'ca10', 'ca11', 'ca12', 'ca13', 'ca14', 'ca15', 'ca16', 'ca17', 'ca18', 
#                'ca19', 'ca20', 'ca21', 'ca22', 'ca23', 'ca24', 'ca25', 'ca26', 'ca27', 'ca28', 'ca29', 'ca30']:
#         source.append(brown.words(fileids=[fileid]))
# for text in source:
#     print len(text)
#     data += ' '.join(text)

data = brown.words(fileids=['ca01', 'ca02', 'ca03', 'ca04', 'ca05', 'ca06', 'ca07', 'ca08', 'ca09', 'ca10'])

print len(data)
        
nonPunct = re.compile('.*[A-Za-z0-9].*')
data = [word for word in data if nonPunct.match(word)]
print len(data)

#data_tokenized = nltk.word_tokenize(data)
data_lowercased = [token.lower() for token in data]

bigrams = nltk.bigrams(data_lowercased)
bigramsFreq = nltk.FreqDist(bigrams)

# w1, w2: sum11 / w1: sum12 / w2: sum21 / none: sum22

(sum11, sum12, sum21, sum22) = 0, 0, 0, 0

bigram_dic = {}

for bg in bigrams:
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
    
sorted_bigram_chisqr = sorted(bigram_dic.iteritems(), key=operator.itemgetter(1))

for entry in sorted_bigram_chisqr:
    if not entry[0][0] in stopwords.words('english') and not entry[0][1] in stopwords.words('english'):
        print entry
        
print time.time() - t1