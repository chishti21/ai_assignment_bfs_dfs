file_data=[]
grid,visited={},{}

with open ('q1.txt','r') as f:
    for line in f:
        tokens=line.strip().split()
        file_data.append(tokens)


for i in range(len(file_data)):
    grid[i]=[]
    visited[i]=[False]*len(file_data[i])
 
for i in range(len(file_data)):
    for j in range(len(file_data[i])):
        grid[i].append(file_data[i][j])
        

def dfs(grid,visited,row,col,max_row,max_col,g,path):
    if col>=max_col:
        return False
    if col<0:
        return False
    if row>=max_row:
        return False
    if grid[row][col]==g:
        print("goal has found")
        print(path)
        return path
    if visited[row][col]==False:
        print(row,"  ",col)
        path.append(grid[row][col])
        visited[row][col]=True
        if dfs(grid,visited,row,col+1,max_row,max_col,g,path):
            return True
        if dfs(grid,visited,row,col-1,max_row,max_col,g,path):
            return True
        if dfs(grid,visited,row+1,col,max_row,max_col,g,path):
            return True
    return False    
    
max_row=len(file_data)
max_col=len(file_data)
g="G"
path=[]
result=dfs(grid,visited,0,2,max_row,max_col,g,path)
print("visited array ")
print(visited)

