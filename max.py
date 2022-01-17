numbers=[2,5,9,88,6,7,33]
def max():
    i=0
    max=0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i=i+1
    print(max)
max()

