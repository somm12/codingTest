n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(input()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt =0
visited = [[0]*m for _ in range(n)]
def dfs(x,y):
    global visited 
    visited[x][y] = 1
    for i in range(4):
        nx = x+ dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and g[nx][ny] == '0':
            dfs(nx,ny)
for x in range(n):
    for y in range(m):
        if not visited[x][y] and g[x][y] == '0':
            dfs(x,y)
            cnt += 1
print(cnt)
# 이코테 DFS예제