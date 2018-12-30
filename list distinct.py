'''count=0
alist=(1,2,4,2,1,3,6,1,5,4,2)
for i in range(0,11):
        for j in range(0,11):
            if(alist[i]==alist[j]):
                count+1
            else:
               blist=(alist[i])
for i in range(0,11):
 print(blist[i])
 print" number of duplicate element"
 print(count)'''
                
count=0
a=[1,2,3,6,4,1,5,9]
for i in range(0,8):
         if(a[i]==a[i+1]):
            count=count+1
print(count)
