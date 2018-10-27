# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:58:32 2018

@author: Brandon
"""

class puppy(object):
    def __init__(self,name,color,legs):
        self.name=name
        self.color=color
        self.legs = legs
        
    #always assign values to method u have
    def bark(self):
        print("iam" ,self.color,self.name, self.legs)
        
        
        
        
        
        
        
        
        
  #  def _del_(self):
   #     print(" dont do ")

puppy1=puppy("runny","black", "4")
puppy1.bark()



#create a class student that has the parameters name age departments and print the names of at least the name of 5 different students


