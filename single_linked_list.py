# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:30:39 2018

@author: Brandon
"""

class node:
    def   __init__(self,data=None):
        self.data=data
        self.next=None
        
        
    def __str__(self):
        return str(self.data)
    
class linked_list:
    def __init__(self):
        self.numofnodes=0
        
        self.head=None
        
    def addfirst(self,data):
        nodeobj=node(data)
        nodeobj.next=self.head
        self.head=nodeobj
        self.numofnodes+=1
        
    def addlast(self,data):
        if self.head is None:
            self.addfirst(data)
            return
        else:
            nodeobj=node(data)
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=nodeobj
            self.numofnodes+=1
            
    def remfirst(self):
        if self.head is None:
            print("cant remove List is already empty")
            return
        else:
            temp=self.head.next
            self.head=temp
            del temp
            self.numofnodes-=1
    
    def remlast(self):
        if self.head is None:
            print("cant remove List is already empty")
            return
        if self.head.next is None:
            self.head=None
            self.numofnodes-=1
            return
   
        temp=self.head
        beforetemp=self.head
        while(temp.next != None):
            beforetemp=temp
            temp=temp.next
        
        beforetemp.next=None
        del temp, beforetemp
        self.numofnodes+=1
        
    def addPos(self,pos,data):
        if pos<=1:
            self.addfirst(data)
            return
        if pos>self.numofnodes:
            self.addlast(data)
            return
        
        temp=self.head
        beforetemp=self.head
        nodeobj=node(data)
        
        for _ in range (pos-1):
            beforetemp.next=temp
            temp=temp.next
        
        nodeobj.next=temp
        beforetemp.next=nodeobj
        self.numofnodes+=1
        del temp,beforetemp
        
        
        
    def printList(self):
        if self.head is None:
            print("cant print!, List is empty")
            return
        temp=self.head
        while(temp):
            print(temp)
            temp=temp.next
    def  totalnodes(self):
        return self.numofnodes
    
linked_list=linked_list()
linked_list.addfirst(2)          
linked_list.remfirst()


linked_list.addfirst(3)
linked_list.addfirst(3)

linked_list.addlast(10)
linked_list.addlast(10)



print(linked_list.totalnodes())        


linked_list.printList()


linked_list.addPos(5,12)
linked_list.printList()

print(linked_list.totalnodes()) 

        
        

    