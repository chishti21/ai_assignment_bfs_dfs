graph={
    'A':[('B',5),('D',3)],
    'B':[('C',1)],
    'C':[('G',8),('E',6)],
    'D':[('E',2),('F',2)],
    'E':[('B',4)],
    'F':[('G',3)],
    'G':[('E',4)]
}

visited=[]
que=[]
def bfs(graph,visited,que,node,goal):
    visited.append(node)
    que.append((node,0))
    while que:
        que=sorted(que,key=lambda x:x[1])
        current_node,current_cost=que.pop(0)
        if current_node==goal:
            print("goal has found ")
            break
        print(current_node,end=" ")
        
        for neighbour,cost in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                que.append((neighbour,cost+current_cost))
                
               
bfs(graph,visited,que,'A','G')    