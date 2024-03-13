from collections import deque
dx = [-1,0,0,1]
dy = [0,-1,1,0]

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

store ={}
p = {}
remainCnt = m
for i in range(1,m+1):
    x,y = map(int,input().split())
    store[i] = [x-1,y-1]

time = 1

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def isArrived():
    global p,remainCnt,g

    tmp = {}
    for num in p:
        x,y = p[num]
        tx,ty = store[num]
        if x==tx and y == ty:# 편의점에 도착했다면, 더이상 그 칸은 못지나감.
            remainCnt -= 1
            g[tx][ty] = -1
        else:
            tmp[num] = [x,y]
    p = tmp

def bfs(x,y,tx,ty):
    q= deque()
    q.append((x,y,[(x,y)]))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,route = q.popleft()
        if x == tx and y == ty:# 가장 먼저 도착했다면, 그 다음 경로가 바로 다음 이동할 칸.
            ax,ay = route[1]
            return [ax,ay]
        for i in range(4):# 상 좌 우 하 우선 순위.
            nx,ny = x+dx[i],y +dy[i]
            if inRange(nx,ny) and g[nx][ny] >= 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny, route+[(nx,ny)]))


def move():
    global p
    tmp = {}
    for num in p:
        x,y = p[num]
        tx,ty = store[num]
        nx,ny = bfs(x,y,tx,ty)
        tmp[num] = [nx,ny]# 다음 이동할 칸.
    p = tmp

def baseCamp():
    global p,g
    sx,sy = store[time]
    q = deque()
    q.append((sx,sy,0))
    visited = [[0]*n for _ in range(n)]
    visited[sx][sy] = 1
    cand =[]
    while q:
        x,y,dist = q.popleft()
        if g[x][y] == 1:
            cand.append((dist,x,y))
            continue
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if inRange(nx,ny) and g[nx][ny] >= 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny,dist+1))
    cand.sort(key=  lambda x:(x[0],x[1],x[2]))# 거리가 짧고 > 행이작고 > 열이 작은 순
    _,x,y = cand[0]
    p[time] = [x,y]
    g[x][y] = -1# 이제 못지나감.

while True:
   
    if remainCnt == 0:# 모두가 편의점으로 이동했다면 종료.
        print(time - 1)
        break
    if len(p)> 0:# 격자에 사람이 존재할 때.
        move()  # 이동하기
        isArrived()# 이동 후, 도착했다면, 도착 처리.
        
    if time <= m:
        baseCamp()# 1분에 1번 사람,,,등 베이스캠프로 들어옴.
       
    time += 1
    