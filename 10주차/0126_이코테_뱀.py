from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
move = deque()
for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

L = int(input())
for _ in range(L):
    x, c= input().split()
    move.append((int(x), c))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
idx = 0
time = 0
snake = deque([(0,0)])

while True:
    time += 1
    # 머리를 꺼낸다.
    x, y = snake[-1]
    nx = x + dx[idx]
    ny = y + dy[idx]
    # 자기 몸이랑 부딪혔을 때
    if (nx,ny) in snake:
        break
    # 벽에 부딪혔을 때
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break
    snake.append((nx,ny))
    # 사과가 아니라면 꼬리를 다시 줄인다. 사과면 0으로 바꾼다.
    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
    else:
        snake.popleft()

    if len(move) > 0 and move[0][0] == time:
        if move[0][1] == 'L':
            idx -= 1
            if idx == -1:
                idx = 3
        else:
            idx += 1
            if idx == 4:
                idx = 0
        move.popleft()
print(time)