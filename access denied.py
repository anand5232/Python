password=input(" enter your password ")
for i in range(0,3,1):
    if(password=='anand'):
        print(" you entered correct password ")
        i=4
    else:
        print(" you entered wrong password ")
        print(" enter the password again you enter the wrong password")
if(i==3):
    print(" access denied")
    
