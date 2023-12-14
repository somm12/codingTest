
from collections import deque
m,n,h = map(int,input().split())

tomato = []

q= deque()

dhxy = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
for a in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int,input().split())))
    tomato.append(box)

    for b in range(n):
        for c in range(m):
            if tomato[a][b][c] == 1:
                q.append((a,b,c))

def bfs():
    while q:
        z,x,y = q.popleft()
        day = tomato[z][x][y]
        for i in range(6):
            nz = z+dhxy[i][0]
            nx = x+dhxy[i][1]
            ny = y+dhxy[i][2]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if tomato[nz][nx][ny] == 0:
                    q.append((nz,nx,ny))
                    tomato[nz][nx][ny] = day + 1

bfs()
answer  = -1
cnt  = 0#안익은 토마토 개수
for z in range(h):
    for x in range(n):
        for y in range(m):
            answer = max(answer,tomato[z][x][y])
            if tomato[z][x][y] == 0:
                cnt += 1

if cnt > 0 and answer != 0: # 안익은 토마토가 하나라도 있다면,
    print(-1)
else:# 모든 토마토가 다 익은 상태였으면 0(즉 최대값) 또는 최소 일수.
    print(answer-1) # 첫 시작이 1부터이므로(익은 토마토 표시 == 지난 일수) 마지막에 -1.
