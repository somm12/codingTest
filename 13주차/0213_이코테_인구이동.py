from collections import deque
import sys
input = sys.stdin.readline

n, L, R = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def process(i,j):
    united = [(i,j)]
    sum_value = g[i][j]
    visited[i][j] = 1
    q = deque([(i,j)])
    num = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if L <= abs(g[x][y] - g[nx][ny]) <= R and not visited[nx][ny]:
                    united.append((nx,ny))
                    sum_value += g[nx][ny]
                    visited[nx][ny] = 1
                    num += 1
                    q.append((nx,ny))
    for x,y in united:
        g[x][y] = sum_value//num

while True:
    index = 0
    visited = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                process(i,j)
                index += 1
    if index == n*n:
        break
    cnt += 1
print(cnt)
