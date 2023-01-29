import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
s, a, b= map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([])
for t in range(1, k+1):
    for i in range(n):
        for j in range(n):
            if g[i][j] == t:
                q.append((i,j,1))

while q:
    x,y,t = q.popleft()
    if t == s+1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if g[nx][ny] == 0:
            g[nx][ny] = g[x][y]
            q.append((nx,ny,t+1))

print(g[a-1][b-1])