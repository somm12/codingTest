from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
g = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    g[a-1][b-1] = 1

L = int(input())
d = deque()
for _ in range(L):
    x,c = input().split()
    d.append((int(x),c))
snake = deque([(0,0)])
time = 0
idx = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while True:
    time += 1
    x, y = snake[-1]
    nx = x + dx[idx]
    ny = y + dy[idx]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break
    if (nx,ny) in snake:
        break
    snake.append((nx,ny))
    if g[nx][ny] == 1:
        g[nx][ny] = 0
    else:
        snake.popleft()
    if len(d) != 0 and d[0][0] == time:
        if d[0][1] == 'D':
            idx += 1
            if idx == 4:
                idx = 0
        else:
            idx -= 1
            if idx == -1:
                idx = 3
        d.popleft()
print(time)
