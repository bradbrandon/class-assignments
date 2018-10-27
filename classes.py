# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:52:25 2018

@author: Brandon
"""

class person:
    l=0
    
    def move(self,legs):
        self.l=legs
        return self.l
    
from person import *
p=person
print(p.move(2))
    
    