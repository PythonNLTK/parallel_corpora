# -*- coding: utf-8 -*- 
from __future__ import division
import codecs
#from collections import defaultdict
                 
def readFile(inputFile):
    
    # data[0] = id, data[1] = string, data[2] = occurrence
    handle = codecs.open(inputFile, 'r', 'utf8')
    data = []
    for line in handle.readlines():
        data.append(line.split(' '))
        
    handle.close()
    
    return data

def readAlignment(inputFile):
    handle = codecs.open(inputFile, 'r', 'utf8')
    data = {}
    
    # line[0] = srcID, line[1] = trgID, line[2] = alignmentScore
    for line in handle.readlines():
        if not line.split(' ')[0] in data and 'e' in line.split(' ')[2]:
            data[line.split(' ')[0]] = (line.split(' ')[1], 0)
        elif not line.split(' ')[0] in data and not 'e' in line.split(' ')[2]:
            data[line.split(' ')[0]] = (line.split(' ')[1], line.split(' ')[2])
        elif line.split(' ')[2] > data[line.split(' ')[0]][1] and not 'e' in line.split(' ')[2]:
            data[line.split(' ')[0]] = (line.split(' ')[1], line.split(' ')[2])
            
    handle.close()
            
    return data

if __name__ == '__main__':
    
    sourceFile = '/home/michi/working/source.txt'
    targetFile = '/home/michi/working/target.txt'
    alignmentFile = '/home/michi/working/aligned.txt'
    
    sourceLang = readFile(sourceFile)
    targetLang = readFile(targetFile)
    aligned = readAlignment(alignmentFile)
        
    for k, v in sorted(aligned.items()):
        print k, v
    
