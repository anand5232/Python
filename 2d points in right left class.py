class points:
    x=0
    y=0
    shift=0;
    def input(self):
        points.x=int(input("enter a first point"));
        points.y=int(input("enter a second point"));
    def calculate(self):
        print("where you want to shift your point  in xy plane")
        print(" 1. for right \n 2. for left \n 3. for top \n 4. for bottom ")
        points.shift=int(input(" enter choice (1 to 4) "))
        if(points.shift==1):
            if(points.x<0):
                points.x=-(points.x)
            print(" your point is shifted right")
            print(points.x,points.y)
        if(points.shift==2):
            if(points.x>0):
                points.x=-(points.x)
            print(" your point is shifted in left direction")
            print(points.x,points.y)
        
        if(points.shift==3):
            if(points.y<0):
                points.y=-(points.y)
            print(" your point is shifted top")
            print(points.x,points.y)
        
            
        if(points.shift==4):
            if(points.y>0):
                points.y=-(points.y)
            print(" your point is shifted bottom")
            print(points.x,points.y)
        
obj=points()
obj.input()
obj.calculate()


                
         
