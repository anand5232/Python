def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
        else:
            return 1

for i in range(1,100,1):
    if prime(i):
        print(i)
