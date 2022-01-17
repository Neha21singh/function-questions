num=int(input("enter your FIRST number....."))
num1=int(input("enter your SECOND number...."))
num3=int(input("enter your THIRD number....."))
def average(num):
    sum=num+num1+num3
    average=sum//3
    return average
print(average(num))

