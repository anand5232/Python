class first():
    def function1(self):
        print(" first class  - this is my first function ")

    def function2(self,string):
        print("first class - my second function :"+string)

class second(first):
    def function3(self):
        print(" second class - function3 ")

    def function4(self):
        first.function2(self)
        print("another class function 2 called")
        
c=first()
c.function1()
c.function2(' anand')
c2=second()
c2.function3()



    
    
