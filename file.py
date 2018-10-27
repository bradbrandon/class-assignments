# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:27:00 2018

@author: Brandon
"""
import os
#//os.chown()change ownership and permissions

#extended modes: wb+ rb+
        
#wb+

os.chdir("C:\\Users\\Brandon\Desktop")
os.getcwd()
filename=input("enter the name of file")
f=open(filename+".txt","w+")#read and write

for i in range(4):
    data=input("enter data \n")
    f.writelines(data)

f.close()
f=open(filename+".txt","r")
f.readlines()
print(f.read())
f=open(filename+".txt","a")
f.write("father")
f=open(filename+".txt","r")
print(f.read())

f.close()
os.rename("C:\\Users\\Brandon\Desktop")







