# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 08:46:05 2017
find Hack words in article
@author: Jerry
"""
# -*- coding: utf-8 -*-
#from google.cloud import language
#Read Files in  File
import numpy as np
import os
import json
#import time
#import dataProcess
#===============================================================================
savename =[]
locdic = {}
loc =[]
keyword = {}
aword =[]
#======================function===================================================
def store(measurements, savefile):   
    with open(savefile, 'w') as f:  
        f.write(json.dumps(measurements))  

def sort_by_value(dic):
    items=dic.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    #newdictloc ={}
    newdicList =[]
    for i in range(len(backitems)):
        newdictloc ={}
        newdictloc[backitems[i][1]] = dic[backitems[i][1]]
        newdicList.append(newdictloc)
    return newdicList
    #return [ backitems[i][1] for i in range(0,len(backitems))]

def readFile(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称  
    s = []  
    for index in range(len(files)): #遍历文件夹  
        if not os.path.isdir(files[index]): #判断是否是文件夹，不是文件夹才打开  
            #f = open(path+"/"+file); #打开文件  
            #iter_f = iter(f); #创建迭代器  
            #str = ""  
            #for line in iter_f: #遍历文件，一行行遍历，读取文本  
            #    str = str + line  
            s.append(files[index]) #每个文件的文本存到list中 
            curname = files[index].strip('.txt')
            savename.append(curname)
    return s

def locGen(filename):
    f1 = open(filename, 'r')
    #strhere = ""
    #inputfile = f1.read().strip('/n');
    inputfile = f1.readlines();
    for index in range(len(inputfile)):
        line = inputfile[index].strip('\n')
        loc.append(line)
        if(locdic.has_key(line)):
            locdic[line] = int(locdic[line]) + 1
        else:
            locdic[line] = 1

def finditem(filename, savefile):
    f1 = open(filename, 'r')
    #strhere = ""
    #inputfile = f1.read().strip('/n');
    inputfile = f1.readlines();
    for line in inputfile:
        content = json.loads(line)
        #print content
        #strhere = content['html']
        print "content",len(content)
        print "len(keys)" ,len(content.keys())
        for key in content.keys():
            if keyword.has_key(key.lower())  :
                aword.append(key.lower())
    print "len(aword)", len(aword)
    np.savetxt(savefile + '_item.txt',aword,fmt='%s',delimiter=' ')
                
            
            
        #print strhere
        #savefile.append(content['id'])
        
    return 1

def processKeyword(filename):
    f1 = open(filename,'r')
    inputfile = f1.readlines()
    #print inputfile
    for line in inputfile:
        cur = line.strip('\n')
        print cur
        keyword[cur.lower()] = 1
    print "keyword", len(keyword)
#===============================================================================
path = "D:/Jerry/1-Study/6-GirlHackthon/ThankyouNingData/ThankyouNing/processeddata/res1/item/" #文件夹目录  
savepath = "D:/Jerry/1-Study/6-GirlHackthon/ThankyouNingData/ThankyouNing/processeddata/res1/resitem/"
keywordfile = "D:/Jerry/1-Study/6-GirlHackthon/keywords.txt"
processKeyword(keywordfile)
filename = readFile(path)
for index in range(len(filename)):
    cur = filename[index].strip('.json')
    print cur
    aword = []
    finditem(path + filename[index], savepath + cur)
