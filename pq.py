l=['p','q']
list=[]
n=5
j=1
while j<=n:
    i=0
    while i<len(l):
        m=l[i]+str(j)
        list.append(m)
        i=i+1
    j=j+1
print(list)