'''
Created on Apr 16, 2014

@author: michi
'''

from nltk.corpus import brown
import time, nltk
from collections import defaultdict
from multiprocessing import Pool

source = """A computer is a general purpose device that can be programmed to carry out a set of arithmetic or logical operations automatically. 
Since a sequence of operations can be readily changed, the computer can solve more than one kind of problem. Conventionally, a computer consists 
of at least one processing element, typically a central processing unit (CPU), and some form of memory. The processing element carries out arithmetic 
and logic operations, and a sequencing and control unit can change the order of operations in response to stored information. Peripheral devices 
allow information to be retrieved from an external source, and the result of operations saved and retrieved. In World War II, mechanical analog 
computers were used for specialized military applications. During this time the first electronic digital computers were developed. Originally 
they were the size of a large room, consuming as much power as several hundred modern personal computers (PCs). Modern computers based on 
integrated circuits are millions to billions of times more capable than the early machines, and occupy a fraction of the space.[2] Simple 
computers are small enough to fit into mobile devices, and mobile computers can be powered by small batteries. Personal computers in their 
various forms are icons of the Information Age and are what most people think of as 'computers.' However, the embedded computers found in 
many devices from MP3 players to fighter aircraft and from toys to industrial robots are the most numerous."""

# 
# t1 = time.time()
# doccount = 0
# for token in data:
#     for fileID in brown.fileids():
#         if token in brown.words(fileids=[fileID]):
#             doccount += 1
# print doccount, time.time() - t1
# 
# t2 = time.time()
# 
# for token in data:
#     print len([file for fileID in brown.fileids() if token in brown.words(fileids=[fileID])])
# 
# print time.time() - t2
# 
# t3 = time.time()
# 
# corpus = defaultdict(list)
# for fileID in brown.fileids():
#     corpus[fileID] = brown.words(fileids=[fileID])
#     
# counter = 0
# for token in data:
#     for fileID in brown.fileids():
#         if token in corpus[fileID]:
#             counter += 1
# 
# print counter, time.time() - t3
# 
# t4 = time.time()
# counter = 0
# 
# for token in data:
#     counter = sum(1 for fileID in brown.fileids() if token in corpus[fileID])
#     print counter
# print time.time() - t4
# 
# t5 = time.time()
# doccount = 0
# for token in data:
#     for fileID in brown.fileids():
#         for word in brown.words(fileids=[fileID]):
#             if word == token:
#                 doccount += 1
#                 break
# print doccount, time.time() - t5


def calcSlow():
    
    doc_dic = defaultdict(list)
    for fileid in brown.fileids():
        for token in brown.words(fileids=[fileid]):
            if token in doc_dic:
                doc_dic[token].append(fileid)
            else:
                doc_dic[token] = [fileid]
    
    return doc_dic
    
def calc(fileid):
    doc_dic = defaultdict(list)
    for token in brown.words(fileids=[fileid]):
        if token in doc_dic:
            doc_dic[token].append(fileid)
        else:
            doc_dic[token] = [fileid]

    return doc_dic

if __name__ == '__main__':
    
    data = nltk.wordpunct_tokenize(source)
    
    t6 = time.time()
    res1 = calcSlow()
    for token in data:
        print len(set(res1[token]))
    print time.time() - t6
    
    t7 = time.time()
    doc_dic = {}
    pool = Pool(processes=2)
    pool.map(calc, brown.fileids())
    print time.time() - t7


