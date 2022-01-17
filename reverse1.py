list= "1234abcd"
def num():
    i=-1
    string=""
    a=[]
    while i>=-len(list):
        string=string+str(list[i])
        a.append(string)
        i=i-1
    print(a,string)
num()