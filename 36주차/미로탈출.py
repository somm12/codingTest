from collections import deque
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    global g
    q = deque()
    q.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0]=1

    while q:
        x,y = q.popleft()
        print(x,y)
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == 1:
                g[nx][ny] = g[x][y] +1
                visited[nx][ny] = 1
                q.append((nx,ny))
            

bfs()
print(g[n-1][m-1])
# 이코테 BFS 예제문제 미로탈출 
