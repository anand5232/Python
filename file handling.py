# here we used write operation in the file
f=open('k1619','w')
f.write("hello")
f.close()


# here we used read mode in the file
f=open('k1619','r')
f.close()

# here we used append mode in the file ..
f=open('k1619','a')
f.write("SUV & ANAND")
f.close()

a=open("k1619.txt",'w') # write mode 
a.write("12.3")
a.close()
a=open("k1619.txt",'r') # read mode
print(a.read())
a.close()
import pickle  # used for different type of datatype and have to convert it into string format used for integer conversion or binary ..because all thing will convert into string 
a=open("k1619.txt",'wb') # wb write in binary format
pickle.dump(12,a)
a.close()
a=open("k1619.txt",'rb')
print(pickle.load(a))
a.close()






















