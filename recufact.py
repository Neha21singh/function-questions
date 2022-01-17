def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
n=int(input("enter your number...."))
z=fact(n)
print("fact",z)
