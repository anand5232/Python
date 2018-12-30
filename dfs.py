graph={'A':['E','B','D'],'B':['A','D','C'],'C':['B'] ,'D':['A','B'],'E':['A']}

def dfs(graph,s):
    visited=[]
    stack=[s]
    while stack:
        node=stack.pop(0)
        if node not in visited:
            visited.append(node)
            stack=stack+graph[node]
    return visited

print(graph)
print(dfs(graph,'A'))
print(dfs(graph,'B'))
print(dfs(graph,'C'))

       
