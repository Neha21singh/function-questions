func1=(20,40,60)
func2=(80,70,100)
def func():
    i=0
    while i<len(func1):
          j=0
          while j<len(func2):
              print(func1[i],func2[j])
              i=i+1
              j=j+1
func()
