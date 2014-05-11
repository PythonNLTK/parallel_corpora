# -*- coding: utf-8 -*- 
from __future__ import division

from nltk import FreqDist
import time, nltk, codecs

def prepareData():
    
    test_set = codecs.open('/home/michi/corpora/testset', 'r', 'utf8')
    data = test_set.read()
    data_tok = nltk.word_tokenize(data)
    pos_tagged = nltk.pos_tag(data_tok)
    
    test_set.close()
    
    return pos_tagged

def calc(tagged_data):
    
    term_freq = []
    #rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(0, len(tagged_data) - 5):
    
#         if (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS') and (pos_tagged[i+4][1] == 'NN' or pos_tagged[i+4][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
#             rule1 += 1
#              
#         elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and pos_tagged[i+2][1] == 'DT' and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS') and (pos_tagged[i+4][1] == 'NN' and pos_tagged[i+4][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
#             rule2 += 1
#              
#         if (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and pos_tagged[i+2][1] == 'DT' and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#             rule3 += 1
#               
#         elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and pos_tagged[i+2][1] == 'IN' and pos_tagged[i+3][1] == 'DT' and (pos_tagged[i+4][1] == 'NN' or pos_tagged[i+4][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0], pos_tagged[i+4][0]))
#             rule4 += 1
#            
#         elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and pos_tagged[i+1][1] == 'IN' and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#             rule5 += 1
        
        if (tagged_data[i][1] == 'NN' or tagged_data[i][1] == 'NNS') and tagged_data[i+1][1] == 'IN' and (tagged_data[i+2][1] == 'NN' or tagged_data[i+2][1] == 'NNS'):
            term_freq.append((tagged_data[i][0], tagged_data[i+1][0], tagged_data[i+2][0]))
            #rule6 += 1
            
#         elif (pos_tagged[i][1] == 'NN' or pos_tagged[i][1] == 'NNS') and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#             rule7 += 1
#              
#         elif pos_tagged[i][1] == 'JJ' and pos_tagged[i+1][1] == 'JJ' and (pos_tagged[i+2][1] == 'NN' or pos_tagged[i+2][1] == 'NNS') and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#             rule8 += 1
#              
#         elif pos_tagged[i][1] == 'JJ' and (pos_tagged[i+1][1] == 'NN' or pos_tagged[i+1][1] == 'NNS') and pos_tagged[i+2][1] == 'IN'  and (pos_tagged[i+3][1] == 'NN' or pos_tagged[i+3][1] == 'NNS'):
#             term_freq.append((pos_tagged[i][0], pos_tagged[i+1][0], pos_tagged[i+2][0], pos_tagged[i+3][0]))
#             rule9 += 1
        
        elif tagged_data[i][1] == 'JJ' and tagged_data[i+1][1] == 'JJ' and (tagged_data[i+2][1] == 'NN' or tagged_data[i+2][1] == 'NNS'):
            term_freq.append((tagged_data[i][0], tagged_data[i+1][0], tagged_data[i+2][0]))
            #rule10 += 1
    
        elif tagged_data[i][1] == 'JJ' and (tagged_data[i+1][1] == 'NN' or tagged_data[i+1][1] == 'NNS') and (tagged_data[i+2][1] == 'NN' or tagged_data[i+2][1] == 'NNS'):
            term_freq.append((tagged_data[i][0], tagged_data[i+1][0], tagged_data[i+2][0]))
            #rule11 += 1
            
        elif (tagged_data[i][1] == 'NN' or tagged_data[i][1] == 'NNS') and (tagged_data[i+1][1] == 'NN' or tagged_data[i+1][1] == 'NNS') and (tagged_data[i+2][1] == 'NN' or tagged_data[i+2][1] == 'NNS'):
            term_freq.append((tagged_data[i][0], tagged_data[i+1][0], tagged_data[i+2][0]))
            #rule13 += 1
            
        elif (tagged_data[i][1] == 'NN' or tagged_data[i][1] == 'NNS') and ( tagged_data[i+1][1] == 'NN' or tagged_data[i+1][1] == 'NNS'):
            term_freq.append((tagged_data[i][0], tagged_data[i+1][0]))
            #rule12 += 1

    return term_freq

def calcFdist(termsList):
    
    return FreqDist(termsList)

def writeToFile(finalTerms):
    
    outFile = '/home/michi/corpora/pos_results.txt'
    
    with codecs.open(outFile, 'w', encoding='utf-8') as resFile:
        for entry in finalTerms.items():
            resFile.write(" ".join(entry[0]) + ',' + str(entry[1]) + '\n')

if __name__ == '__main__':
    
    t1 = time.time()
    
    tagged = prepareData()  
    scores = calc(tagged)
    fdist = calcFdist(scores)
    writeToFile(fdist)

    print time.time() - t1

#print rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13


    
    
    