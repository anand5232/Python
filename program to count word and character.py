f=open("test.txt","w")
f.write("hello how are you ")
f.close()

f=open("test.txt","r")
data=f.read()
count=0
for i in data:
    if(i==" "):
            count=count+1
j=len(data)
character=j-count
        
        
print(" number of character are ",character)       
print(" number of word are ",count)
f.close()
