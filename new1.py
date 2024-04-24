grid={}
visited={}
que=[]
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


for i in range(3):
    grid[i]=[]
    visited[i]=[]

for i in range(rows):
    for j in range(cols):
        if i == 1 and j == 1:
            grid[i].append(1)
        else:
            grid[i].append(0)


grid[g_r][g_c] = 100
print(grid)
#print(visited)                
def bfs(grid,que,i,j,visited):
    visited[i].append(j)
    que.append(i)
    que.append(j)
    while que:
        row=que.pop(0)
        column=que.pop(0)
        #print(row,column)
        if grid[row][column]==100:
            print("goal has found ",row,column)
            print("path follwed ")
            print(road_path)
            break
        #print(grid[row][column])
        
        if column+1<cols:
            if row>=0 and grid[row][column+1]!=1:
                if column+1  not in visited[row]:
                    visited[row].append(column+1)
                    road_path.append((row,column+1))
                que.append(row)
                que.append(column+1)
                    
        if row-1>=0:
            if grid[row-1][column]!=1:
                if column not in visited[row-1]:
                 visited[row-1].append(column)
                 road_path.append((row-1,column))
                 que.append(row-1)
                 que.append(column)
                 
        if row-1>=0 and column+1<cols:
            if grid[row-1][column+1]!=1:
                if column+1 not in visited[row-1]:
                    visited[row-1].append(column+1)
                    road_path.append((row-1,column+1))
                    que.append(row-1)
                    que.append(column+1)

bfs(grid,que,s_r,s_c,visited)
#print(visited)
                         