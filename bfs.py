class A():
    def creategraph(self):
            graph={'A':['B','E','F'],'B':['A','E','C','D'],'C':['B'] ,'D':['B'],'E':['A','B'],'F':['G']}
            n=len(graph)
            print(graph)
            print('total lenght of the graph = ',n)
            for i in range(n):
                print(graph[i])

b=A()
b.creategraph()

class B()



   

       
