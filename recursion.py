i=0
def myfun():
    global i
    i=i+1
    print("neha",i)
    myfun()
myfun()