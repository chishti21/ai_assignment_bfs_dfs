graph = {
    'A': [('B', 5), ('D', 3)],
    'B': [('C', 1)],
    'C': [('G', 8), ('E', 6)],
    'D': [('E', 2), ('F', 2)],
    'E': [('B', 4)],
    'F': [('G', 3)],
    'G': [('E', 4)]
}
heuristic_values = {'A': 8, 'B': 7, 'C': 6, 'D': 5, 'E': 4, 'F': 3, 'G': 0}

visited=[]
que=[]

def astar(graph,visited,goal,start,que):
    visited.append(start)
    h=heuristic_values[start]
    que.append((start,0,h))
    while que:
        que.sort(key=lambda x:x[2])
        current_node, cost, _ = que.pop(0)
        if current_node==goal:
            print("goal has found")
            break
        print(current_node,end=" ")
        
        for neighbour,edge_cost in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                new_cost=cost+edge_cost
                h=heuristic_values[neighbour]
                que.append((neighbour,new_cost,new_cost+h))

astar(graph,visited,'G','A',que)                        