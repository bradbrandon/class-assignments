# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:37:19 2018

@author: Brandon
"""
student={'Name':'', 'surname':'','contact_details':'','gender':'','Dob':'','program':''}
studentlist=[]
def inputn():
    
    name= input("enter  the name:" )
    student['name']= name
    
    Surname= input("enter  the  surname:" )
    student['surname']= Surname
    contact= input("enter  the contact_details:" )
    student['contact_details']= contact
    gender= input("Enter  the gender:" )
    student['gender']= gender
    Dob= input("Enter  the date of birth:" )
    student['Dob']= Dob
    program = input("Enter the program of study:" )
    student['program']= program
    
    
   
    
    
while (len(studentlist)<2):
     inputn()
     studentlist.append(student)
     
     
studentlist
 

   


