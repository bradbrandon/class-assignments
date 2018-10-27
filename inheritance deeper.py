# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:24:18 2018

@author: Brandon
"""

class base():
    def __init__(self):
        print(" Mina ngubase")
        
    def f(self):
        print(" my name is miracle")
        


class sub(base):
    
    
    def __init__(self):
        super().__init__()
        print("I am sub")

    def f(self):
        print(" my name is miracle , i dont like choir")
    
    


s=sub()
