list=[29,17,10,22,24]
i=0
a=[]
while i<len(list):
    a.append(list[i])
    a.append(a)
    i=i+1
print(a)
