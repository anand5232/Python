max=0
min=0
alist = [1,2,3,4,5,9,7,8,6]
for i in range(0,9):
    for j in range(0,9):
        print(alist[i],alist[j])
        if(alist[i]>alist[j]):
            max=alist[i]
            print(max)
        if(alist[i]<alist[j]):
            min=alist[i]
print" maximum is = "
print(max)
print" minimum is = "
print(min)
        
