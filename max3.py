a=[2,3,-5,32,9,45,22]
def show():
    i=0
    max=0
    sec=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
        j=0
        sec=0
        third=0
        while j<len(a):
            if max>a[j] and a[j]>sec:
                sec=a[j]
            elif sec>a[j]and a[j]>third:
                third=a[j]
            j=j+1
    print(max) 
    print(sec)
    print(third)
show()
