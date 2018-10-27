# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 07:26:55 201
"""

#code for input

malelist=[]
femalelist=[]
namelist=[]
counter=0

    
    
    
    
    
 #function which checks for age and accepts 5 females
def males():
    print("enter all females:")
    while (len(malelist) <5 ):
    
        print("enter your age")
        age=int(input())

        if (age>=23) :
            print("enter your name:")
            malelist.append(input())
            
           
        else :
            print("invalid age")
 
    else:
        print(" male list is full")

 #function which checks for age and accepts 5 females   
def females():
    print("enter all females:")
    while (len(femalelist)<5 ):
    
        print("enter your age")
        fage=int(input())

        if (fage>25) :
            print("enter  your name")
            femalelist.append(input())
            
        
         
        
        else :
            print("invalid age")
 
    else:
        print(" female list is full")



 #code to call both function for capturing 10  males and females
