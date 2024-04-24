grid={}
visited={}
for i in range(3):
    grid[i]=[]
    visited[i]=[]

road_path=[]

file_data=[]
with open ('ass.txt','r') as f:
    for line in f:
        tokens=line.strip().split()
        file_data.append(tokens)

#print(file_data[5][0])
rows=int(file_data[0][0])
cols=int(file_data[1][0])
s_r=int(file_data[2][0])
s_c=int(file_data[3][0])
g_r=int(file_data[4][0])
g_c=int(file_data[5][0])



for i in range(rows):
    for j in range(cols):
        if i==1 and j==1:
            grid[i].append(1)
        else:
            grid[i].append(0)




grid[g_r][g_c]=100
print(grid)


def dfs(row,col,destination,grid,max_depth):
    if row<0:
        return False
    if col>=cols:
        return False
    
    if grid[row][col]==1:
        return False
    print("checking for destination",row," ",col)
    if grid[row][col]==destination:
        print("path grid")
        return True
    if max_depth<=0:
        return False
    if dfs(row,col+1,destination,grid,max_depth-1):
        road_path.append((row,col+1))
        return True
    if dfs(row-1,col,destination,grid,max_depth-1):
        road_path.append((row-1,col))
        return True
    if dfs(row-1,col+1,destination,grid,max_depth-1):
        road_path.append((row-1,col+1))
        return True
        
def idfs(row,col,destination,grid,max_depth):
    for i in range(max_depth):
        if dfs(row,col,destination,grid,i):
            return True
    return False

 
if idfs(s_r,s_c,100,grid,9):
    print("path has found") 
    #print(road_path)
else:
    print("path not found")      
                    