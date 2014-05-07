# -*- coding: utf-8 -*- 
from __future__ import division
import codecs
from collections import defaultdict
from operator import itemgetter

                 
def readFile(inputFile):
    
    # data[0] = id, data[1] = string, data[2] = occurrence
    handle = codecs.open(inputFile, 'r', encoding='utf-8')
    data = []
    for line in handle.readlines():
        data.append([int(line.split(' ')[0]), line.split(' ')[1]])
        
    handle.close()
    
    return data

def readAlignment(inputFile):
    handle = codecs.open(inputFile, 'r', encoding='utf-8')
    data = defaultdict(list)
    
    # line[0] = srcID, line[1] = trgID, line[2] = alignmentScore
#     for line in handle.readlines():
#         if not line.split(' ')[0] in data and 'e' in line.split(' ')[2]:
#             data[line.split(' ')[0]] = (line.split(' ')[1], 0)
#         elif not line.split(' ')[0] in data and not 'e' in line.split(' ')[2]:
#             data[line.split(' ')[0]] = (line.split(' ')[1], line.split(' ')[2])
#         elif line.split(' ')[2] > data[line.split(' ')[0]][1] and not 'e' in line.split(' ')[2]:
#             data[line.split(' ')[0]] = (line.split(' ')[1], line.split(' ')[2])

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
    for entry in src:
        print entry[1], trg.index(alignedIDs[entry[0]])#, trg[alignedIDs[entry[0]][0]][1]
        try:
            alignedToks.append((entry[1], trg[alignedIDs[entry[0]][0]][1]))
        except Exception:
            pass

    return alignedToks

def writeToFile(finalMerge):
    
    outFile = '/home/michi/corpora/merged.txt'
    with codecs.open(outFile, 'w', encoding='utf-8') as myFile:
        for entry in finalMerge:
            myFile.write(entry[0] + ',' + entry[1] + '\n')#.encode('UTF-8'))

if __name__ == '__main__':
    
    sourceFile = '/home/michi/corpora/source.txt'
    targetFile = '/home/michi/corpora/target.txt'
    alignmentFile = '/home/michi/corpora/aligned.txt'
    
    sourceLang = readFile(sourceFile)
    targetLang = readFile(targetFile)
    aligned = readAlignment(alignmentFile)
    
    print aligned.items()[:10]
    print targetLang[:10]
    print targetLang.index(788)
    finalMerge = alignTokens(sourceLang, targetLang, aligned)   
    
    #writeToFile(finalMerge)
#     for entry in finalMerge:
#         print entry[0], entry[1].encode("UTF-8")
#     
