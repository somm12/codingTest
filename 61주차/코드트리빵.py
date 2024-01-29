from collections import deque

g = []
dx = [-1,0,0,1]
dy = [0,-1,1,0]
goal = {}
people = {}

n,m = map(int,input().split())
cnt = m

for _ in range(n):
    g.append(list(map(int,input().split())))

for i in range(1,m+1):
    x,y =map(int,input().split())
    goal[i] = [x-1,y-1]


def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def move():
    global people

    for num in people:# 다음으로 이동할 위치 구하기
        nx,ny = bfs(num)
        people[num] = [nx,ny]

def bfs(num):# 최단 거리로 이동했을 시, 다음위치.
    tx,ty = goal[num]
    x,y = people[num]
    q = deque()
    q.append((x,y,[(x,y)]))
    visited =[[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,route = q.popleft()
        if tx == x and ty == y:
            return route[1]
        for i in range(4):
            nx,ny = x+dx[i], y +dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx,ny, route+[(nx,ny)]))
def isStore():# 이미 도착시, 더이상 못지나감. 도착했으니 cnt -1
    global people, g,cnt
    tmp = {}
    for num in people:
        x,y = people[num]
        tx,ty = goal[num]
        if x == tx and y == ty:
            g[x][y] = -1
            cnt -= 1
        else:
            tmp[num] = [x,y]
    people = tmp

def baseCamp():# 베이스캠프로 이동. 목표 편의점과 가장 가까운 곳 찾아서 이동.
    global people,g
    tx,ty = goal[time]
    cand = []# 후보
    q= deque()
    q.append((tx,ty,0))
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1
    while q:
        x,y,dist = q.popleft()
        if g[x][y] == 1:
            cand.append((dist,x,y))
            continue
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] =1
                q.append((nx,ny,dist+1))
    cand.sort(key= lambda x : (x[0],x[1],x[2]))
    ntx,nty = cand[0][1],cand[0][2]
    g[ntx][nty] = -1
    people[time]= [ntx,nty]

time = 1
while True:
    if len(people) > 0:
        move()
        isStore()
      
    if time <= m:
        baseCamp()

    if cnt == 0:
        break
 
    time += 1

print(time)

