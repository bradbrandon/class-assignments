# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:21:14 2018

@author: Brandon
"""
listname=[]
listcontact=[]
listgender=[]
listdob=[]
listprog=[]
finallist={}

def nams():
    print(dir(finallist))
    print(finallist.update())
    while (len(listname)<1):
         print("enter your name and surname:")
         temp=input()
         listname.append(temp)
    
       
       
def getall():
    x=0
    while (len(listprog)<10):
        print("enter contact details for:",listname[x])
        temp =input()
        listcontact.append(temp)
        print("enter gender for :",listname[x])
        temp=input()
        listgender.append(temp)
        print("enter date of birth for:",listname[x])
        temp=input()
        listdob.append(temp)
        print("enter program of study for:",listname[x])
        temp=input()
        listprog.append(temp)
        x+=1
        
        
        
def printall():
    x=0
    while (x<10): 
        finallist(listname[x] + listcontact[x] &"  :" & listgender[x] &" :"& listdob[x]&": "&listprog[x])
        print("details for student:",listname[x])
        print(listcontact[x],"  ",listgender[x]," ",listdob[x], " ",listprog[x])
        x+=1
        
      
def main():
    nams()
    getall()
    printall()
    
        
   

    
    
    
    
    
    
