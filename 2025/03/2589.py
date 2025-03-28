from collections import deque

n,m = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

g = []
for _ in range(n):
    g.append(list(input()))

answer = 0
    
def bfs(sx,sy,visited):
    global answer
    visited[sx][sy] = 1
    q = deque()
    q.append((sx,sy))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == "L":# 육지인 곳, 이미 방문한 곳을 피해서 최단거리 구하기.
                visited[nx][ny] = visited[x][y] + 1
                answer = max(answer,visited[nx][ny])
                q.append((nx,ny))
  
for i in range(n):
    for j in range(m):
        if g[i][j] == "L":# 육지인 곳을 중심으로 최단거리를 구하기.
            visited = [[0]*m for _ in range(n)]
            bfs(i,j,visited)

print(answer - 1)
# 백준 보물섬