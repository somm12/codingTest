import sys
input = sys.stdin.readline
from collections import deque
R,C = map(int,input().split())
g = []
target = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

waterQ = deque()
swanQ = deque()

waterTempQ = deque()
swanTempQ = deque()

visited = [[0]*C for _ in range(R)] # melting에 사용
visitedSwan = [[0]*C for _ in range(R)] # move에 사용
for i in range(R):
    g.append(list(input().rstrip()))
    for j in range(C):
        if g[i][j] == 'L':
            swanX,swanY = i,j
        if g[i][j] == 'L' or g[i][j] == '.':# 백조가 있는 위치도 물위 이기 때문에 주의.
            visited[i][j] = 1
            waterQ.append((i,j))


def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

def melting():# 빙판 녹이기.
    global g

    while waterQ:
        x,y = waterQ.popleft()
        for i in range(4):
            nx,ny =x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny]:
                if g[nx][ny] == 'X':
                    waterTempQ.append((nx,ny))
                    g[nx][ny] = '.'
                    visited[nx][ny] = 1



def move():# 백조 이동.
   
    while swanQ:
        x,y = swanQ.popleft()
        for i in range(4):
            nx,ny =x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visitedSwan[nx][ny]:
                visitedSwan[nx][ny] = 1
                if g[nx][ny] == '.':
                    swanQ.append((nx,ny))
               
                elif g[nx][ny] == 'L':
                    return True
                elif g[nx][ny] == 'X':
                    swanTempQ.append((nx,ny))
        
    return False

t = 0
swanQ.append((swanX,swanY))
visitedSwan[swanX][swanY] = 1
while True:
    if move():
        print(t)
        break
    
    melting()
    waterQ = waterTempQ# 다음번째 melting 시키기 위한 물의 좌표를 담은 tempQ를 waterQ에 할당
    swanQ = swanTempQ# 다음에 이동할 수 있는 좌표를 담은 tempQ을 담기.
    waterTempQ = deque()# 다시 비우기.
    swanTempQ = deque()
  
    
    t += 1
# 백준 백조의 호수
# 이전 날에 이어서 이동할 수 있도록 큐를 두 개 사용.