# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:39:02 2018

@author: Brandon
"""

class farmer:
    def regester(self):
        print("enter the following details to register for a loan:")
        self.Name=input("enter your name and Surname:")
        self.contact_details=input("Enter your contact details:")
        self.asserts_owned=input("enter asserts you own:")
        self.farmsize=input("enter farm size in hectares:")
        self.purpose=input("enter purpose of loan:")
        
    def appplication(self):
        self.amount=0
        self.monthlyincome=int(input("enter purpose of loan:"))
        amount=int(input("enter the amount you want to borrow:"))
        self.deposit= 0.2*amount
        
        self.choice=int(input("enter 1 if can can deposit" ,deposit, "and 2 if no right now")
   
        if self.farmsize>50000 and self.choice==1:
            print("application accepted")
            
        else:
            print("application denied")
            
zbankloan=farmer()

            
            
        
    
        
