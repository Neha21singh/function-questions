def double():
    list=[1, 2, 3, 3, 3, 3, 4, 5]
    c=[]
    i=0
    while i<len(list):
        if list[i] not in c:
            c.append(list[i])
        i=i+1  
    print(c)
double()