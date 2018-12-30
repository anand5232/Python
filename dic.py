d={}
t=int(input(" enter how many values you want to enter "))
for i in range(t):
    l=[]
    a=input('enter the node')
    nb=int(input("enter number of neighbours"))
    for i in range(nb):
        n=input("enter neighbours value")
        l.append(n)
    d[a]=l
print(d)
    
