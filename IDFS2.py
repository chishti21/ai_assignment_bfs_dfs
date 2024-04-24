Goal="G"
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}


def dfs(current_node,destination,graph,max_depth):
    if current_node==destination:
        return True
    if max_depth<=0:
        return False
    for neighbour in graph[current_node]:
        if dfs(neighbour,destination,graph,max_depth-1):
            return True
    return False

    
def idfs(current_node,destination,graph,max_depth):
    for i in range(max_depth):
        if dfs(current_node,destination,graph,i):
            return True
    return False
 

if idfs('A','G',graph,4):
    print("path has found")
else:
    print("path has not found")    