def num():
    num=int(input("enter your number"))
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print("it is perfect")
    else:
        print("it is not perfect")
num()
