# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:34:27 2018

@author: Brandon
"""
#create a class student that has the parameters name age departments and print the names of at least the name of 5 different students
class student(object):
    def __init__(self,name,age,dep):
        self.name=name
        self.age=age
        self.dep = dep
        
    #always assign values to method u have
    def printdet(self):
        print("the student details are" ,"Name:"+self.name,"age:"+self.age,"Department:"+ self.dep)
        
        
    
count=1
studlist=[]

while (count<=5):
      
      
    stud=student((input("enter name:",)),(input("enter age:",)),(input("enter department:",)))
    studlist.append(stud)
    stud.printdet()
    print("enter the next student:")
    count+=1
    
    
for studlist[count] in studlist:
    
    if  (stud.age>
for stud in studlist:
    
    print("details fo students are ","name"+stud.name,"Age:"+stud.age,"department"+stud.dep)



    

#create a class student that has the parameters name age departments and print the names of at least the name of 5 different students
