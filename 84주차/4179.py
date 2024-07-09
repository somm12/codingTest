import sys
input = sys.stdin.readline

from collections import deque

g = []
fire = deque()
jh = deque()
R,C = map(int,input().split())
visited = [[0]*C for _ in range(R)]# 지훈 

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(R):
    g.append(list(input()))
    for j in range(C):
        if g[i][j] == 'J':
            visited[i][j] = 1
            jh.append((0,i,j))
        elif g[i][j] == 'F':
            fire.append((0,i,j))

def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

def fMove():
    while fire and fire[0][0] == time:
        t,x,y = fire.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] == '.':# 불도 . 이 있는 곳으로만 이동 가능.
                g[nx][ny] = 'F'# F를 할당하면서, 방문처리겸 할 수 있음.
                fire.append((t+1,nx,ny))
def jMove():
    while jh and jh[0][0] == time:# 매분마다 이동하므로, 현재 분인 부분만 이동.
        t,x,y = jh.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not inRange(nx,ny):
                return t+1
            if not visited[nx][ny] and g[nx][ny] == '.':
                visited[nx][ny]= 1
                jh.append((t+1,nx,ny))
    if len(jh) > 0:# 더 이동할 칸이 남음.
        return "CONTINUE"
    return "IMPOSSIBLE"# 이동 가능한 칸이 없음.

time = 0
while True:
    fMove()# 불 이동 
    rv = jMove()# 지훈 이동.
    time += 1
    if rv == "IMPOSSIBLE":# 탈출 불가.
        print(rv)
        break
    elif rv == "CONTINUE":# 계속 이동 가능.
        continue
    elif rv > 0:# 탈출 성공.
        print(rv)
        break
   
