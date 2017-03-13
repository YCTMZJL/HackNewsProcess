# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:09:38 2017
data process for Hack news
@author: Jerry
"""
# Imports the Google Cloud client library
from google.cloud import language
#Read Files in  File
import numpy as np
import os
import json
import time
#import dataProcess
#============================global==================================================
item = []
itemdict ={}
loc =[]
dictloc = {}
org = []
savename =[]
strhere = ""
org2 =[]
#======================function===================================================
def store(measurements, savefile):   
    with open(savefile, 'w') as f:  
        f.write(json.dumps(measurements))  
#map={}
#ranked = sorted(map.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) //排序可行
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

def findentities(filename, language_client):
    f1 = open(filename, 'rb')
    lines = f1.readlines()
    for line in lines:
        print len(line)
        document = language_client.document_from_text(line)
        entities = document.analyze_entities().entities
        for entity in entities:
            if entity.entity_type == 'LOCATION':
                loc.append(entity.name)
                if(dictloc.has_key(entity.name)):
                    dictloc[entity.name] = dictloc[entity.name] + 1
                else:
                    dictloc[entity.name] = 1
                #curdictloc ={}
                #curdictloc["location"] = entity.name
                #dicloc.append(curdictloc)
            if entity.entity_type == 'ORGANIZATION':
                #tmp = []
                #tmp.append(entity.name)
                #tmp.append(entity.metadata.get('wikipedia_url', '-'))
                tmp ={}
                tmp['orgname'] = entity.name
                tmp['wiki'] = entity.metadata.get('wikipedia_url', '-')
                org.append(tmp)
                #org.append(entity.name + entity.metadata.get('wikipedia_url', '-'))
            else:
                #tmp = {}
                #tmp['itemname'] = entity.name
                #tmp['wiki'] = entity.metadata.get('wikipedia_url', '-')
                #item.append(tmp)
                #item.append(entity.name)
                if(not itemdict.has_key(entity.name)):
                    itemdict[entity.name] ={}
                    itemdict[entity.name]['wiki']  = entity.metadata.get('wikipedia_url', '-')
    if(len(lines) == 0):
        return 0
    else:
        return 1
############3
#strhere = ""
def findentities2(filename, language_client):
    f1 = open(filename, 'rb')
    strhere = ""
    lines = f1.readlines()
    for lindex in range(len(lines)):
        print lindex
        strhere = strhere + ' ' + lines[lindex]
        #print strhere
    document = language_client.document_from_text(strhere)
    entities = document.analyze_entities().entities
    for entity in entities:
        if entity.entity_type == 'LOCATION':
            loc.append(entity.name)
            if(dictloc.has_key(entity.name)):
                dictloc[entity.name] = dictloc[entity.name] + 1
            else:
                dictloc[entity.name] = 1
        if entity.entity_type == 'ORGANIZATION':
            tmp ={}
            tmp['orgname'] = entity.name
            tmp['wiki'] = entity.metadata.get('wikipedia_url', '-')
            org.append(tmp)
            #org.append(entity.name + entity.metadata.get('wikipedia_url', '-'))
        else:
            if(not itemdict.has_key(entity.name)):
                itemdict[entity.name] ={}
                itemdict[entity.name]['wiki']  = entity.metadata.get('wikipedia_url', '-')
    if(len(lines) == 0):
        return 0
    else:
        return 1

############3

def findentities3(filename, language_client): # input is Json
    f1 = open(filename, 'r')
    strhere = ""
    #inputfile = f1.read().strip('/n');
    inputfile = f1.readlines();
    for line in inputfile:
        #print lindex
        #print line
        content = json.loads(line)
        strhere = content['html']
        #print strhere
        #savefile.append(content['id'])
        time.sleep(1)
        document = language_client.document_from_text(strhere)
        time.sleep(1)
        entities = document.analyze_entities().entities
        #print entities
        countn = 1
        org3 =[]
        loc3 = []
        itemdict3 ={}
        for entity in entities:
            countn = countn + 1;
            #if()
            print entity.name
            if entity.entity_type == 'LOCATION':
                loc3.append( (entity.name).lower() )
                if dictloc.has_key( (entity.name).lower() ):
                    dictloc[(entity.name).lower()] = int(dictloc[(entity.name).lower()]) + 1
                else:
                    dictloc[(entity.name).lower()] = 1
            if entity.entity_type == 'ORGANIZATION':
                tmp ={}
                tmp['orgname'] = (entity.name).lower()
                tmp['wiki'] = entity.metadata.get('wikipedia_url', '-')
                org3.append(tmp)
                #org.append(entity.name + entity.metadata.get('wikipedia_url', '-'))
            else:
                if(not itemdict3.has_key((entity.name).lower())):
                    itemdict3[(entity.name).lower()] ={}
                    itemdict3[(entity.name).lower()]['wiki']  = entity.metadata.get('wikipedia_url', '-')
            
        if(len(loc) > 0) :
            #np.savetxt(savepath + 'loc/' +savename[index] +'_loc.txt',loc,fmt='%s',delimiter=' ')
            store(loc, savepath + 'loc/' + savename[index]+ content['id']+'_loc.json')
        if(len(itemdict) > 0) :
                    #np.savetxt(savepath + savename[index] +'_item.json',itemdict,fmt='%s',delimiter=' ')
            store(itemdict, savepath + 'item/'+ savename[index] + content['id']+'_item.json')
        if(len(org) > 0) :
                    #np.savetxt(savepath + 'org/'+ savename[index] +'_org.json',item,fmt='%s',delimiter=' ')
            store(org, savepath + 'org/' + savename[index] + content['id']+'_org.json')
        time.sleep(10)           
        print len(org), len(loc), len(itemdict)

    #if(len(lines) == 0):
    #    return 0
    #else:
    #    return 1
    return 1

#=========================================================================
#path = "D:/Jerry/1-Study/6-GirlHackthon/data2/" #文件夹目录  
path = "../data2/" #文件夹目录  
#savepath = 'D:/Jerry/1-Study/6-GirlHackthon/processeddata/res1/'
savepath = '../processeddata/res1/'
filename = readFile(path)
language_client = language.Client()
#findentities(filename[0], language_client)
#np.savetxt(savePath+'.txt',item,fmt='%s',delimiter=',')
for index in range(len(filename)):
    print "index ", filename[index]
    #loc = []
    #org = []
    #item =[]
    #itemdict ={}
    findentities3(path + filename[index], language_client) 
    '''
    try:
        if( findentities3(path + filename[index], language_client) == 1) :
            #cursavepath = savename[index]
            print "enter"
            if(len(loc) > 0) :
                #np.savetxt(savepath + 'loc/' +savename[index] +'_loc.txt',loc,fmt='%s',delimiter=' ')
                store(loc, savepath + 'loc/' + savename[index] +'_loc.json')
                if(len(itemdict) > 0) :
                    #np.savetxt(savepath + savename[index] +'_item.json',itemdict,fmt='%s',delimiter=' ')
                    store(itemdict, savepath + 'item/'+ savename[index] +'_item.json')
                if(len(org) > 0) :
                    #np.savetxt(savepath + 'org/'+ savename[index] +'_org.json',item,fmt='%s',delimiter=' ')
                    store(org, savepath + 'org/' + savename[index] +'_org.json')
    except:
        with open('../wrong/wrong_list.txt','a') as wf:
            wf.write((filename[index]+'\n'))
    '''
highscoreLoc = sort_by_value(dictloc)
np.savetxt(savepath + 'highscoreLoc.json',highscoreLoc,fmt='%s',delimiter=' ')
#store(highscoreLoc, savepath +'highscoreLoc.json')
#record again

    

    

