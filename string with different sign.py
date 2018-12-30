print"enter the string here"
a=input()
for i in a:
    if(i=='#'):
        i='@'
    if(i>=0 or i<=9):
        i=','
print(a)
    
