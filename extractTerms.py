# -*- coding: utf-8 -*- 
from __future__ import division
import codecs, ast
from collections import defaultdict

def readSingleWords():
    
    source = '/home/michi/corpora/tfidf_results.txt'
    singleWordList = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            singleWordList.append(line.split(','))
        
    # [0] = string, [1] = score
    return singleWordList

def readMultiWords():
    
    source = '/home/michi/corpora/pos_results.txt'
    multiWordList = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            multiWordList.append([line.split(',')[0].split(' '), line.split(',')[1].rstrip('\n')])
            
    # [0] = term, [1] = count
    return multiWordList

def readTokenAlignment():
    
    source = '/home/michi/corpora/merged.txt'
    alignedTokens = []
    with codecs.open(source, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            alignedTokens.append(line.split(','))

    return alignedTokens

def filterSingleTerms(singleWordTerms):
    # use only terms whose score is higher than 10
    
    return [word for word in singleWordTerms if ast.literal_eval(word[1]) >= 10]
    
def filterMultiTerms(multiWordTerms):
    # use only terms with occurrence higher than 500 and return term without occurrence
    
    temp = []
    for entry in multiWordTerms:
        try:
            if int(entry[1]) >= 500:
                temp.append(entry[0])
        except Exception:
            pass

    return temp

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

def writeToFile(alignedSingle, alignedMulti):
    
    outFile = '/home/michi/corpora/final_results.txt'
    
    with codecs.open(outFile, 'w', encoding='utf-8') as myFile:
        for single in alignedSingle:
            myFile.write(' '.join(single))
            myFile.write('\n')
            
        for multi in alignedMulti:
            myFile.write(' '.join(multi))
            myFile.write('\n')

if __name__ == '__main__':
       
    singleWordTerms = readSingleWords()
    filteredSingleTerms = filterSingleTerms(singleWordTerms)
    multiWordTerms = readMultiWords()
    filteredMultiTerms = filterMultiTerms(multiWordTerms)
    
    alignedData = readTokenAlignment()
    alignedSingleTerms = alignSingleTerms(filteredSingleTerms, alignedData)
    alignedMultiTerms = alignMultiTerms(filteredMultiTerms, alignedData)

    print alignedSingleTerms[:10], len(alignedSingleTerms)
    #print alignedMultiTerms[:10], len(alignedMultiTerms)
     
    writeToFile(alignedSingleTerms, alignedMultiTerms)
    
    