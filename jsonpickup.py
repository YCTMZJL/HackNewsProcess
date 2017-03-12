# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:03:42 2017

@author: Jerry
For Information picking up
"""
import json

inputfile = open('D:\\Jerry\\1-Study\\6-GirlHackthon\\data\\stories','r').read().strip('\n')
for i in range( len(inputfile) ):
    content = json.loads(inputfile[i])
#print content['type']

