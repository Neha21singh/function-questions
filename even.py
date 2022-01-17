n=int(input("enter your numer"))
def even():
    if n%2==0:
        print(n,"even")
    else:
        print(n,"odd")
        return even
even()