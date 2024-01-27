from collections import deque

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
mx = [-1,-1,-1,0,1,1,1,0]
my = [-1,0,1,1,1,0,-1,-1]
time = [[0]*m for _ in range(n)]

def selectAttack():#공격자 선정
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cand.append([g[x][y], time[x][y], x+y,x,y])
    cand.sort(key = lambda x: (x[0],-x[1], -x[2],-x[4]))
    x,y = cand[0][3],cand[0][4]
    return [x,y]

def selectTarget():# 대상자 선정
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0 and [ax,ay] != [x,y]:
                cand.append([g[x][y], time[x][y], x+y,x,y])
    cand.sort(key = lambda x: (-x[0], x[1], x[2],x[4]))
    x,y = cand[0][3],cand[0][4]
    return [x,y]

def beam():# 레이저 공격
    q = deque()
    visited = [[0]*m for _ in range(n)]
    q.append((ax,ay,[(ax,ay)]))
    visited[ax][ay] = 1
    while q:
        x,y,route = q.popleft()
        if x == tx and y == ty:
            return route
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            nx %=n# 맵을 벗어나도 연결됨.
            ny %= m
            if g[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny, route+[(nx,ny)]))# 경로 저장하기.
    return False# 공격대상자 접근 불가면 False

def bomb():# 포탄 공격.
    tmp = []
    for i in range(8):
        nx,ny = tx+mx[i],ty+my[i]
        nx %= n
        ny %= m
        
        if [nx,ny] != [ax,ay] and g[nx][ny] > 0:# 공격자 제외한 것 중에서 부서지지 않은 포탑 주변 8방향.
            tmp.append((nx,ny))
    return tmp
def organize(arr):
    global g
    s = set()
    for x,y in arr:
        s.add((x,y))
    s.add((ax,ay))
    s.add((tx,ty))
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0 and (x,y) not in s:
                g[x][y] += 1
def check():
    cnt = 0
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cnt += 1
    if cnt <= 1:
        return True
    return False
for turn in range(1,k+1):
    if check():# 포탑 1개 남으면 즉시 종료.
        break
    ax,ay = selectAttack()
    time[ax][ay] = turn
    g[ax][ay] += (n+m)

    tx,ty = selectTarget()
    
    route = beam()
    
    if route != False:
        g[tx][ty] -= g[ax][ay]
        route = route[1:-1]# 중간 경로들도 공격 받는다.
        for x,y in route:
            g[x][y] -= (g[ax][ay]//2)
            if g[x][y] < 0:
                g[x][y] = 0

        
        organize(route)
    else:
        route = bomb()
        
        g[tx][ty] -= g[ax][ay]
        for x,y in route:
            g[x][y] -= (g[ax][ay]//2)
            if g[x][y] < 0:
                g[x][y] = 0
        organize(route)


    if g[tx][ty] < 0:
        g[tx][ty] = 0

for x in range(n):
    for y in range(m):
        answer = max(answer,g[x][y])
print(answer)
