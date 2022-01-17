list= "1234abcd"
def num():
    i=-1
    string=""
    while i>=-len(list):
        string=string+str(list[i])
        i=i-1
    print(string)
num()