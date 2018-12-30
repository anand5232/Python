def functions(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    dev=a/b
    return add,sub,mul,dev

print(" enter two number ")
a=int(input())
b=int(input())
t=functions(a,b)
for i in t:
    print(i)
    print()
