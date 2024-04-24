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
    print("checking for destination",current_node)
    if current_node==destination:
        return True
    if max_depth<=0:
        return False
    
    for node in graph[current_node]:
        if dfs(node,destination,graph,max_depth-1):
            return True
    return False    

def ids(current_node,destination,graph,max_depth):
    for i in range(max_depth):
        if dfs(current_node,destination,graph,i):
            return True  
    return False        


if not ids('A','E',graph,4):
    print("path is not available")
else:
    print(" path is available")    

                