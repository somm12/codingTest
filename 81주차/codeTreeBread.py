from collections import deque
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
target = {}# 사람들이 목표로하는 편의점 위치
p = {}# 격자에 있는 사람들 위치 정보
for num in range(1,m+1):
    x,y = map(int,input().split())
    target[num] = [x-1,y-1]

time = 1
remain = m
dx = [-1,0,0,1]# 상 좌 우 하 우선순위.
dy = [0,-1,1,0]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y,tx,ty):
    q = deque()
    visited = [[0]*n for _ in range(n)]
    for i in range(4):
        nx,ny= x+dx[i],y+dy[i]
        if inRange(nx,ny) and g[nx][ny] >= 0:
            q.append((nx,ny,i))# 현재 위치 다음의 방향을 저장해둠.
            visited[nx][ny] = 1
    while q:
        x,y,nd = q.popleft()
        if x == tx and y == ty:# 목표 위치에 도달 했을 때 가장 먼저 popleft된 nd가 다음 이동할 방향.
            return nd
        for i in range(4):
            nx,ny= x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] >= 0:
                q.append((nx,ny,nd))
                visited[nx][ny] = 1

def baseCamp():
    global g,p
    sx,sy = target[time]
    q = deque()
    q.append((sx,sy,0))
    cand = []
    visited = [[0]*n for _ in range(n)]
    visited[sx][sy] = 1
    while q:
        x,y,dist = q.popleft()
        if g[x][y] == 1:
            cand.append((dist,x,y))
        for i in range(4):
            nx,ny= x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] >= 0:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = 1
    cand.sort(key = lambda x:(x[0],x[1],x[2]))# 거리가 작고 행이작고 열이작은 순서.
    _,x,y= cand[0]
    g[x][y] = -1
    p[time] = [x,y]


def move():
    global p,remain,g
    tmp = {}
    for num in p:
        x,y = p[num]
        tx,ty = target[num]
        nd = bfs(x,y,tx,ty)
        nx,ny = x+dx[nd],y+dy[nd]
        tmp[num] = [nx,ny]
    p = tmp

def isArrive():
    global p,g,remain
    tmp = {}
    for num in p:
        x,y = p[num]
        tx,ty = target[num]
        if x == tx and y == ty:
            g[x][y] = -1
            remain -= 1
        else:
            tmp[num] = [x,y]
    p = tmp

while remain > 0:

    if len(p) > 0:
        move()# 모두 이동.
        isArrive()# 혹시 편의점에 도착했다면, 해당 자리는 지나갈 수 없음.

    if remain == 0:# 이동해야할 사람이 없다면 종료
        print(time)
        break

    if time <= m:# m분이하라면 time번째 사람이 베이스캠프에 입장
        baseCamp()


    time += 1
# 코드트리 빵 문제.