# -*- coding: utf-8 -*- 
from __future__ import division
import codecs

def readSingleWords():
    
    source = '/home/michi/corpora/tfidf_results.txt'
    singleWordList = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            singleWordList.append(line.split(','))
            #singleWordList[line.split(',')[0]] = line.split(',')[1]
        
    # [0] = string, [1] = score
    return singleWordList

def readMultiWords():
    
    source = '/home/michi/corpora/pos_results.txt'
    multiWordList = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            multiWordList.append(line.split(',')[0].split(' '))
            
    # [0] = term, [1] = count
    return multiWordList

def readTokenAlignment():
    
    source = '/home/michi/corpora/merged.txt'
    alignedTokens = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            alignedTokens.append(line.split(','))

    return alignedTokens

def filterSingleTerms():
    #to be done
    pass
    
def filterMultiTerms():
    #to be done
    pass

def alignSingleTerms(singleWordTerms, alignedData):
    
    alignedSingleTerms = []
    for term in singleWordTerms:
        for entry in alignedData:
            if term[0] == entry[0]:
                alignedSingleTerms.append(entry)
                
    return alignedSingleTerms

def alignMultiTerms(multiWordTerms, alignedData):
    
    alignedMultiTerms = []
    for entry in multiWordTerms:
        l = len(entry)
        for i in range(0, len(alignedData) - 1):        
            if l == 2:
                if entry[0] == alignedData[i][0] and entry[1] == alignedData[i+1][0]:
                    alignedMultiTerms.append((alignedData[i][0], alignedData[i+1][0], alignedData[i][1], alignedData[i+1][1]))
            
            elif l == 3:
                if entry[0] == alignedData[i][0] and entry[1] == alignedData[i+1][0] and entry[2] == alignedData[i+2][0]:
                    alignedMultiTerms.append((alignedData[i][0], alignedData[i+1][0], alignedData[i+2][0], alignedData[i][1], alignedData[i+1][1], alignedData[i+2][1]))
            
            elif l == 4:
                if entry[0] == alignedData[i][0] and entry[1] == alignedData[i+1][0] and entry[2] == alignedData[i+2][0] and entry[3] == alignedData[i+3][0]:
                    alignedMultiTerms.append((alignedData[i][0], alignedData[i+1][0], alignedData[i+2][0], alignedData[i+3][0], alignedData[i][1], alignedData[i+1][1], alignedData[i+2][1], alignedData[i+3][1]))  
        
    return alignedMultiTerms

if __name__ == '__main__':
    
    singleWordTerms = readSingleWords()
    multiWordTerms = readMultiWords()
    alignedData = readTokenAlignment()
    #alignedSingleTerms = alignSingleTerms(singleWordTerms, alignedData)
    alignedMultiTerms = alignMultiTerms(multiWordTerms, alignedData)
    
#     for term in singleWordTerms:
#         if term in alignedData:
#             print term
    
    print singleWordTerms[0]
    print multiWordTerms[:10]
    print alignedData[0]
    #print alignedSingleTerms[:20]
    print alignedMultiTerms[:10]
    
    