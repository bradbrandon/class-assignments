#code for input

mlist=[]
flist=[]
namelist=[]
count=0

    
    
    
    
    
    
#def minput():
#    while (len(mlist) <5 ):
    
     #   print("enter your age")
#        age=int(input())
#
      #  if (age>=23) :
#            print("enter your name:")
#            mlist.append(input())
            
           
       # else :
        #    else:
       # print(" male list is full")
        
        
    
def finput():
    while (len(flist)<5 ):
    
        print("enter your age")
        fage=int(input())

        if (fage>=23) :
            print("enter  your name")
            flist.append(input())
            
        
         
        
        else :
            print("invalid age")
 
    else:
        print(" female list is full")
    

print("enter  m or f for gender:")
gender=input()
if (gender=='m'):
    minput()
       
       
        
elif (gender=='f'):
        finput()
              
else :
    print("invalid input")

    

    