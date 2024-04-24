graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

# visited=[]
# stack=[]

# def dfs(stack,visited,graph,node):
#     visited.append(node)
#     stack.append(node)
#     s=stack.pop(-1)
#     print(s,end="  ")
    
#     for neighbour in graph[s]:
#         if neighbour not in visited:
#             dfs(stack,visited,graph,neighbour)
# dfs(stack,visited,graph,'A')        

    
    