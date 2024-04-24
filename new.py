# grid = {}
# visited = {}

# cost=0
# for i in range(3):
#     grid[i] = []
#     visited[i] = []

# for i in range(3):
#     for j in range(3):
#         if i == 1 and j == 1:
#             grid[i].append(1)
#         else:
#             grid[i].append(0)

# grid[0][2] = 100 
# print(grid)

# def dfs(visited, grid, i, j):
#     global cost
#     if i < 0:
#         #print("Goal has not been found", i, j)
#         return False
#     if j >= 3:
#         #print("Goal has not been found", i, j)
#         return False
    
#     if grid[i][j] == 100:
#         print("Goal has been found", i, j, "cost",cost)
#         return True
#     if grid[i][j] == 1:
#         return False
#     if j not in visited[i]:
#         visited[i].append(j)
#         if dfs(visited, grid, i, j + 1):
#             cost+=2
#             return True
#         if dfs(visited, grid, i - 1, j):
#             cost+=2  
#             return True
#         if dfs(visited, grid, i - 1, j + 1):
#             cost+=3  
#             return True
#     return False

# result=dfs(visited, grid, 2, 0)
# if result==False:
#     print("goal has not found")
# else:
#     print(visited)



grid = {}
visited = {}
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

#print(rows,cols,"  ",s_r,s_c,"  ",g_r,g_c)

cost = 0
for i in range(rows):
    grid[i] = []
    visited[i] = []

for i in range(rows):
    for j in range(cols):
        if i == 1 and j == 1:
            grid[i].append(1)
        else:
            grid[i].append(0)

grid[g_r][g_c] = 100
print(grid,"print grid")

def dfs(visited, grid, i, j):
    global cost  

    if i < 0:
        return False
    if j >= cols:
        return False

    if grid[i][j] == 100:
        print("Goal has been found", i, j)
        print("Cost:", cost)
        return True
    if grid[i][j] == 1:
        return False
    if j not in visited[i]:
        visited[i].append(j)
        road_path.append((i,j))
        if dfs(visited, grid, i, j + 1):
            cost += 2
            print(cost, "cost is")
            return True
        if dfs(visited, grid, i - 1, j):
            cost += 2
            print(cost, "cost is")
            return True
        if dfs(visited, grid, i - 1, j + 1):
            cost += 3
            print(cost, "cost is")
            return True
    return False

result = dfs(visited, grid, s_r, s_c)
if result == False:
    print("Goal has not been found")
else:
    print("path followed  ",road_path)
