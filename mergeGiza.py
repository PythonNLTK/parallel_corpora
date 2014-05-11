# -*- coding: utf-8 -*- 
from __future__ import division
import codecs
from collections import defaultdict
from operator import itemgetter

                 
def readFile(inputFile):
    
    # data[0] = id, data[1] = string, data[2] = occurrence
    handle = codecs.open(inputFile, 'r', encoding='utf-8')
    data = {}
        
    for line in handle.readlines():
        data[int(line.split(' ')[0])] = line.split(' ')[1]
        
    handle.close()
    
    return data

def readAlignment(inputFile):
    handle = codecs.open(inputFile, 'r', encoding='utf-8')
    data = defaultdict(list)

    for line in handle.readlines():
        if not line.split(' ')[0] in data:
            data[line.split(' ')[0]].append((line.split(' ')[1], float(line.split(' ')[2].rstrip('\n'))))
        else:
            data[line.split(' ')[0]].append((line.split(' ')[1], float(line.split(' ')[2].rstrip('\n'))))
            
    temp = {}
    for k, v in data.items():
        temp[int(k)] = int(max(v,key=itemgetter(1))[0])
                    
    handle.close()
            
    return temp

def alignTokens(src, trg, alignedIDs):
    alignedToks = []

    for entry in alignedIDs.items():
        if entry[0] in src and entry[1] in trg:
            alignedToks.append((src[entry[0]], trg[entry[1]]))

    return alignedToks

def writeToFile(finalMerge):
    
    outFile = '/home/michi/corpora/merged.txt'
    with codecs.open(outFile, 'w', encoding='utf-8') as myFile:
        for entry in finalMerge:
            if entry[0].isalpha():
                myFile.write(entry[0].lower() + ',' + entry[1] + '\n')

if __name__ == '__main__':
    
    sourceFile = '/home/michi/corpora/source.txt'
    targetFile = '/home/michi/corpora/target.txt'
    alignmentFile = '/home/michi/corpora/aligned.txt'
    
    sourceLang = readFile(sourceFile)
    targetLang = readFile(targetFile)
    aligned = readAlignment(alignmentFile)
       
    finalMerge = alignTokens(sourceLang, targetLang, aligned)   
    writeToFile(finalMerge)
     
