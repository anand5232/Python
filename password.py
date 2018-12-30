print" enter the password"
passw=input()
l=len(passw)
b=0
c=0
d=0
if(l>=5):
    for i in passw :
        if(i>='A' or i<='Z'):
            b=b+1
        if(i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*'):
            c=c+1
        if(i>=0 or i<=9):
            d=d+1
else:
    
if(b>=1 or c>=1 or d>=1):
    print"password generated"
else:
    print" invalid password please reenter the password"
            
            
