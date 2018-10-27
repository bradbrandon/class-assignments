# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:50:09 2018

@author: Brandon
"""

class Loan:
    def __init__(self,name,contact,asserts_owned,farmsize,purpose,amount,monthly_income):
        self.name=name
        self.contact=contact
        self.asserts_owned=asserts_owned
        self.farmsize=farmsize
        self.purpose=purpose
        self.amount=amount
        self.monthly_income=monthly_income
        
        
    def compute_application(self):
        if int(self.amount)>300 or int(self.farmsize)>200 or int(self.monthly_income)>100:
            print("application accepted")
        else :
            print("appication denied")
        

Zbbankloan=Loan(input("enter the farmer name:"),input("enter the farmers contact details:"),
                input("enter the farmers asserts owned:"),int(input("enter the farmsize")),input("enter the purpose"),
                int(input("enter the amount to be borrowed")),int(input("enter the farmer monthly_income")))


Zbbankloan.compute_application()

        
        
        
