def primeornot(n):
    """ this function is used for the prime number """
    flag=0
    i=2
    while(i<=n):
        if(n%i==0):
            flag=0
            break
        else:
            flag=1
            break
        i=i+1
    return flag

for i in range(2,10,1):
    x=primeornot(i)
    if(x==1):
        print(i)
        
    
