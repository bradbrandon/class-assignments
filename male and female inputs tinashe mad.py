# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:14:57 2018

@author: tinashe Madivani
"""


male_list=[]
def male_input():
    while (len(male_list)<5):
        print("Pliease enter your age" )
        male_age =int(input())
        
        if (male_age>=25):
            print("Please your your name")
            male_list.append(input())
            
        else: print("invalid age ")
        
    else: print("male list is full")
    
    
#defining function for females 
female_list=[]
def female_input():
    while (len(female_list)<5):
        print("Please enter your age" )
        female_age =int(input())
        
        if (female_age>=25):
            print("Please your your name")
            female_list.append(input())
            
        else: print("invalid age ")
        
    else: print("female list is now full")
        
    
#print("PLease enter m if you are male and please enter f if you are female")
#gender=input()
#if (gender=="m"):
 #       male_input()
        
#elif (gender=="f"):
#            
#else:
 #       print("invalid input")
