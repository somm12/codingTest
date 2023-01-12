import sys
sys.setrecursionlimit(10**6)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[0] * n for _ in range(n)]
def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        else:
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                dfs(nx,ny)
res1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            res1 += 1

visited = [[0] * n for _ in range(n)]
res2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            res2 += 1    
print(res1,res2)      

# 방문하지 않았을 때만 재귀.