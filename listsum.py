list= [1, 2, 3, 4, 5,1]
def numbers():
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    print(sum)
numbers()