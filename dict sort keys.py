# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:01:59 2018

@author: Brandon
"""

peson={"name":"jodza",
       "age":"30",
       "regno":"H1701C"}

keys=list(peson.keys())
keys.sort()
new_dict={}
for key in keys:
    print("Insertong keys",key)
    new_dict[keys]=peson[key]
    print(new_dict)