from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
mx = [-1,-1,0,1,1,1,0,-1]
my = [0,1,1,1,0,-1,-1,-1]

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

time = [[0]*m for _ in range(n)]

def inRange(x,y):
    return 0 <= x < n and 0<= y < m

def isFinish():
    cnt = 0
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cnt += 1
    
    return cnt == 1

def attacker():
    global g,time
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y]>0:

                cand.append((g[x][y], time[x][y], x+y,x,y))
    cand.sort(key = lambda x :(x[0], -x[1], -x[2],-x[4]))
    x,y = cand[0][3],cand[0][4]
    g[x][y] += (n+m)

    time[x][y] = nth
    return [x,y]

def target():
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y]>0 and [x,y] != [ax,ay]:
                cand.append((g[x][y], time[x][y], x+y,x,y))
    cand.sort(key = lambda x :(-x[0], x[1], x[2],x[4]))
    x,y = cand[0][3],cand[0][4]
    return [x,y]

def beam():
    global g
    q = deque()
    q.append((ax,ay,[(ax,ay)]))
    visited = [[0]*m for _ in range(n)]
    visited[ax][ay] = 1
    cand = []
    while q:
        x,y,route = q.popleft()
        if x == tx and y == ty:
            cand.append(route)
            break
        for i in range(4):
            nx,ny= (x+dx[i])%n, (y+dy[i])%m # dx,dy는 우선순위 순서로 설정! 우 하 좌 상
            if g[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx,ny,route + [(nx,ny)]))
                visited[nx][ny] = 1
    if len(cand) == 0:
        return False

    
    g[tx][ty] -= g[ax][ay]
    num = g[ax][ay]//2 # 최단 경로에도 피해 줌.

    route = cand[0]

    tmp = route[1:-1]
    for x,y in tmp:
        g[x][y] -= num
    route = set(route)
    for x in range(n):# 정비하기.
        for y in range(m):
            if g[x][y] >0 and (x,y) not in route:
                g[x][y] += 1
    return True
def bomb():# 주위 8방향도 피해.
    global g
    g[tx][ty] -= g[ax][ay]
    s = set()
    s.add((tx,ty))
    s.add((ax,ay))

    for i in range(8):
        nx,ny = (tx+mx[i])%n, (ty+my[i])%m
        if [nx,ny] != [ax,ay] and g[nx][ny] > 0:# 공격자 제외한 주위 8방향.
            g[nx][ny] -= (g[ax][ay]//2)
            s.add((nx,ny))
    
    for x in range(n):# 정비하기
        for y in range(m):
            if g[x][y] > 0 and (x,y) not in s:
                g[x][y] += 1
    
                
for nth in range(1,k+1):
    if isFinish():# 부서지지 않은 포탑이 1개가 되면 종료.
        break
    ax,ay = attacker()# 공격자 선정
    
    tx,ty = target()# 공격 대상자 선정
    

    flag = beam()# 공격 & 정비
    

    if not flag:
        bomb() # 공격 & 정비

  
   
answer = 0
for arr in g:
    answer = max(answer,max(arr))
print(answer)