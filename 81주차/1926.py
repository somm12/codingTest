import sys
input= sys.stdin.readline
sys.setrecursionlimit(10000*250)
n,m  = map(int,input().split())
g = []
total = 0
maxSize =0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in  range(n):
    g.append(list(map(int,input().split())))
visited =[[0]*m for _ in range(n)]

def dfs(x,y):
    visited[x][y] = 1
    cnt = 1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == 1:
            cnt += dfs(nx,ny)
    return cnt

for x in range(n):
    for y in range(m):
        if not visited[x][y] and g[x][y]== 1:
            maxSize = max(maxSize, dfs(x,y))
            total +=1
print(total)
print(maxSize)
#백준.