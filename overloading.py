# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:26:20 2018
method overloading
@author: Brandon
"""

class Something:
    
    def Add(self,x,y):
        return x+y
    
    def greeting(self,name=None):
        if name is not None:
            print("hello "+name)
        else:
            print("hello")
    
d=Something()
#d.Add(5,7)
d.greeting()
d.greeting('kkkkkkkk')
    