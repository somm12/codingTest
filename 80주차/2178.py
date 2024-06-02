from collections import deque
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(input()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0]*m for _ in range(n)]
def bfs(x,y):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny =x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1# 최단 거리 구하기. 
                q.append((nx,ny))
bfs(0,0)
print(visited[n-1][m-1])# 마지막 칸에 저장된 것이 곧 최단거리.
# 백준 bfs 미로탐색.