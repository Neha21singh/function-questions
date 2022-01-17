def even(n):
  if n==1:
    return 1
  else:
    return (n%2==0,n-1)
n=int(input("enter the number.."))
x=even(n)
print(x)