from collections import deque

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
people = {}
desti = {}
for num in range(1,m+1):
    x,y = map(int,input().split())
    desti[num] = [x-1,y-1]
time =1
dx = [-1,0,0,1]
dy = [0,-1,1,0]

cnt = m

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y,tx,ty):# 목적지 까지 가장 최소거리, 상 좌 우 하 방향 순서로. 다음 가게될 좌표 반환.
    q= deque()
    q.append((x,y,[(x,y)]))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,route = q.popleft()
        if x == tx and y == ty:
            return route[1]
        for i in range(4):
            nx= x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and g[nx][ny] >= 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                if len(route) == 1:
                    q.append((nx,ny,route+[(nx,ny)]))
                else:
                    q.append((nx,ny,route))

def move():# 이동.
    global people
    tmp = {}
    for num in people:
        x,y = people[num]
        tx,ty = desti[num]
        nx,ny = bfs(x,y,tx,ty)
        tmp[num] = [nx,ny]
    people = tmp

def check():# 도착했는지 체크.
    global g, people,cnt
    tmp = {}
    for num in people:
        x,y = people[num]
        tx,ty = desti[num]
        if x == tx and y == ty:
            cnt -= 1# 도착했으니 -1.
            g[tx][ty] = -1
        else:
            tmp[num] = [x,y]
    people = tmp

def baseCamp(num):# 베이스캠프에 들어가기
    global g,people
    tx,ty = desti[num]
    q = deque()
    q.append((tx,ty,0))
    visited  = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1
    cand = []
    while q:
        x,y,dist = q.popleft()
        if g[x][y] == 1:
            cand.append((dist,x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] >= 0:
                visited[nx][ny] = 1
                q.append((nx,ny,dist+1))
    cand.sort(key=lambda x:(x[0], x[1],x[2]))
    _,x,y = cand[0]
    people[num] = [x,y]
    g[x][y]= -1

while True:

    if len(people) > 0:
        move()
        check()

        if cnt == 0:# 모두가 도착했다면, 종료.
            print(time)
            break
    if time <= m:
        baseCamp(time)
    time += 1
