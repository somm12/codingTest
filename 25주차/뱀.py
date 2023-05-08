from collections import deque
from collections import defaultdict
n = int(input())
snake = deque()
snake.append((0,0))
s = defaultdict(int)
s[(0,0)] += 1
d = 0
g = [[0]*n for _ in range(n)]
k = int(input())
change = {}
for _ in range(k):# 사과 위치 할당
    a,b = map(int,input().split())
    g[a-1][b-1] = 1

L = int(input())
for _ in range(L):# t초뒤 c방향으로 회전
    t,c = input().split()
    change[int(t)] = c
dx = [0,1,0,-1] # 우 하 좌 상(오른쪽으로 90도씩 회전, 왼쪽 방향으로는 왼쪽으로 90도씩 회전)
dy = [1,0,-1,0]
time = 0

while True:
    time += 1
    x,y = snake[-1]
    nx = x + dx[d]
    ny = y + dy[d]
    snake.append((nx,ny))
    s[(nx,ny)] += 1
    if nx < 0 or nx >= n or ny < 0 or ny >= n: # 벽에 부딪혔다면 종료
        break
    if s[(nx,ny)] > 1:# 자기 몸에 부딪혔다면 종료(이미 존재하는 좌표 값이 있을시)
        break

    if g[nx][ny] == 1: # 사과가 있다면, 사과가 없어지고 꼬리는 그대로
        g[nx][ny] = 0
    else:
        sx,sy = snake[0] # 꼬리 부분
        snake.popleft() # 사과가 없다면, 꼬리 부분 빈칸.
        del s[(sx,sy)]

    if time in change: # 현재 방향 전환하는 time이라면 그에 맞춰서 90도 회전.
        if change[time] == 'D':
            d += 1
            if d > 3:
                d = 0
        else:
            d -= 1
            if d < 0:
                d = 3
print(time)