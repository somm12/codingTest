from collections import deque
n = int(input())
g = []

maxV = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        maxV = max(maxV, g[i][j])

def bfs(x,y,visited):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] > h:
                visited[nx][ny] = 1
                q.append((nx,ny))
answer = 0

for h in range(maxV+1):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and g[x][y] > h:
                bfs(x,y,visited)
                cnt += 1
    answer = max(answer,cnt)

print(answer)
# 백준 안전 영역.