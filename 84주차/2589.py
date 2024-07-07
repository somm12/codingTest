from collections import deque
n,m = map(int,input().split())
g = []
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    g.append(list(input()))

def inRange(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy,0))
    visited = [[0]*m for _ in range(n)]
    visited[sx][sy] = 1
    maxV = 0
    while q:
        x,y,dist = q.popleft()
        maxV = max(maxV,dist)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 'L':
                visited[nx][ny] = 1
                q.append((nx,ny,dist+1))
    return maxV

for x in range(n):
    for y in range(m):
        if g[x][y] == 'L':# 해당 육지에서의 모든 다른 육지까지의 최단거리를 구하고, 그 중 최대 거리를 구한다.
            answer = max(answer,bfs(x,y))
print(answer)
# 백준 보물섬