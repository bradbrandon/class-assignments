# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:20:43 2018

@author: @author: Tanaka Muchandibaya H170154c
"""
class cantern:
    
        time=0
        item=[]
        price=0
        def __init__(self,studname,studsurname,studco_detail,studprogram):
        
            
            self.studname= studname
            self.studsurname=studsurname
            self.studco_detail= studco_detail
            self.studprogram=studprogram
            
            
            
        def booking(self):
           self.time =input("Enter 'launch' for launch and 'dinner' for evining ticket:" )
            
            
        def pricing(self):
            print( "items availble  on the menu  are :")
            print( "1:Sadza and  beef :$1")
            print( "2:rice and  chicken :$0.50")
            print( "3:Sadza  and  soup :$.30")
            print( "4:rice and soup:$.30")
            
            
            itemnum=input("Enter item number")
                        
            if (itemnum==1):
                self.item.append("Sadza and  beef ")
                self.price+=1
            elif itemnum==2:
                self.item.append("rice and  chicken ")
                self.price+=0.50
            elif itemnum==3:
                self.item.append("Sadza  and  soup ")
                self.price+=0.30
            elif itemnum==4:
                self.item.append("rice and soup ")
                self.price+=0.30
            
                         
                      
        def printall(self):  
            print("Reciept for : ",self.studname ,"  ",self.studsurname,
                  "\n contact details:",self.studco_detail,"program of study: ",
                  self.studprogram )
            print("Items: ",self.item)
            print("time of validity: ",self.time)
            print("total price: $ ",self.price)
            
#code           
       
    #  def __init__(self,studname,studsurname,studco_detail,studprogram,time):

hit_canteen=cantern(input("enter the student name",),input("enter the student surname",),
                    input("enter the student contact details",),
                    input("enter the program of study",))

hit_canteen.booking()
hit_canteen.pricing()

print("")
hit_canteen.printall()




                      
     
     