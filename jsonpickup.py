# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:03:42 2017

@author: Jerry
For Information picking up
"""
import json
def store(measurements, savefile):   
    with open(savefile, 'w') as f:  
        f.write(json.dumps(measurements))  
        
dictcom =[]
inputfile = open('comment.json','r').readlines()
for inputf in inputfile:
    content = json.loads(inputf)
    tmp = {}
    tmp['by'] = content['by']
    tmp['text'] = content['text']
    dictcom.append(tmp)
store(dictcom, 'commit2.json')
#print content['type']

