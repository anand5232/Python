print("enter the string here")
a=input()
b=""
c=""
l=len(a)
for i in range(0,l):
    if(a[i]=='a' or a[i]=='e' or a[i]=='u' or a[i]=='i' or a[i]=='o'):
            b[i]=b+a
    else:
        c=c+a[i]
print(" vowels = ")
print(b)
print(" consonant = ")
print(c) 

// other option
 alternative of this program will be

we can take i and check with direct into string
for i in a
    then same procedure
