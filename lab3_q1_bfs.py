visited, grid = {}, {}
file_data = []

with open("q1.txt", 'r') as f:
    for line in f:
        tokens = line.strip().split()
        file_data.append(tokens)

for i in range(len(file_data)):
    grid[i] = []
    visited[i] = [False] * len(file_data[i])

for i in range(len(file_data)):
    for j in range(len(file_data[i])):
        grid[i].append(file_data[i][j])


def bfs(grid,visited,max_row,max_col,row,col,goal):
    que=[]
    que.append((row,col))
    visited[row][col]=True
    while que:
        row,col=que.pop(0)
        print(grid[row][col],end=" ")
        
        if grid[row][col]==goal:
            print("goal has found")
            return True
        if col+1<max_col and not visited[row][col+1]:
            que.append((row,col+1))
            visited[row][col+1]=True
        if row+1<max_row and not visited[row+1][col]:
            que.append((row+1,col))
            visited[row+1][col]=True
        if row-1>=0 and not visited[row-1][col]:
            que.append((row-1,col))
            visited[row-1][col]=True
        if col-1>=0 and not visited[row][col-1]:
            que.append((row,col-1))
            visited[row][col-1]=True  
    print("goal not found")
    return False                     
max_row=len(file_data)
bfs(grid,visited,max_row,max_row,0,2,'G')
