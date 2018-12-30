f1=open('file1.txt','w')
f1.write('hello python programer')
f1.close
a=input('enter string to delete')
f1=open('file1.txt','x')
s=f1.read()
i=s.find(a)
l=len(a)
t=s[0:i]+s[l+1:]
f1.close
f1=open('file1.txt','w')
f1.write(t)
f1.close()

