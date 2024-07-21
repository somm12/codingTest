from collections import deque
from typing import ValuesView

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(input()))

answer =0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs(x,y):
    
    q = deque()
    q.append((x,y))
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    maxDist = 0
    while q:
        x,y = q.popleft()
        maxDist = max(maxDist,visited[x][y])
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] =='L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

    return maxDist-1

for x in range(n):
    for y in range(m):
        if g[x][y] == 'L':
            answer = max(answer,bfs(x,y))
print(answer)
# 백준 보물섬. -> 최단 거리 중 최대 거리를 구함.
# 모든 육지를 출발점으로 두어서 최단거리 구하기.