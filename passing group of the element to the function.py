""" function to calculate the sum and average of the list and then print with the help of
      function """
def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum=sum+i
    avg=0
    avg=sum/n
    return sum,avg 

print(" enter the numbers you want to enter ")
lst=[int(x) for x in input().split()]
x,y=calculate(lst)
print('total',x)
print('average',y)
