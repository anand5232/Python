def fact(n):
    facto=1
    while(n>0):
        facto=facto*n
        n=n-1
    return facto

a=int(input(" enter the number to findout the factorial of that number "))
x=fact(a)
print(" factorial of the function ")
print(x)


