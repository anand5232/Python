class time:
    second=15
    minute=16
    hour=2

    def addtime(self):
       a=int(input("enter the second you want to add"))
       time.second=a+time.second
       b=int(input("enter the minute you want to add"))
       time.minute=b+time.minute
       c=int(input("enter the hour you want to add"))
       time.hour=c+time.hour
    def display(self):
        print("second =",time.second)
        print(" minute = ",time.minute)
        print(" hour =",time.hour)
obj=time()
obj.display()
obj.addtime()
obj.display()
       
        
