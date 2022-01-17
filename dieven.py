list=[1,2,3,4,5,6,7,8,9]
def show():
    i=1
    a=[]
    while i<len(list):
        if i%2==0:
            a.append(i)
        i=i+1
    print(a)
show()