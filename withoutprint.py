def eveodd(a):
  
   i=0
   c=[]
   d=[]
   while i<len(a):
    
    if a[i]%2==0:
        c.append(a[i])
    else:
        d.append(a[i])
    i=i+ 1 
   return(c) 
b=eveodd([12,2,3,4,5,6]) 
print(b)
