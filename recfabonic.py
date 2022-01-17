def fab(n):
    if n==1:
        return 1
    else:
        return(n+fab(n-1))
n=int(input("enter your number...."))
z=fab(n)
print("fab",z)

