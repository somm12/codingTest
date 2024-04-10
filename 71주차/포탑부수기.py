from collections import deque

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx= [0,1,0,-1,1,1,-1,-1]# 우 하 좌 상 우선순위. + 대각선 4방향.
dy = [1,0,-1,0,1,-1,-1,1]
attime = [[0]*m for _ in range(n)]

def isFinish():# 부서지지않은 포탑이 1개 남을 시 종료.
    cnt =0
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cnt += 1
    return cnt == 1

def selectAttacker():# 공격자 선정.
    global g, attime
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cand.append((g[x][y],attime[x][y],x+y,y))# 공격력이 작고 > 최근에 공격했으며 > 행과열의 합이 크고, 열이 큰. 기준으로 선정.
    cand.sort(key=lambda x:(x[0],-x[1],-x[2],-x[3]))
    _,_,total,y = cand[0]
    x= total-y
    g[x][y] += (n+m)
    attime[x][y] = nth
    return [x,y]

def selectTarget():# 공격 대상자 선정.
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0 and [x,y] != [ax,ay]:# 공격자 제외.
                cand.append((g[x][y],attime[x][y],x+y,y))
    cand.sort(key = lambda x:(-x[0],x[1],x[2],x[3]))
    _,_,total,y = cand[0]
    x = total - y
    return [x,y]

def beam():# 레이저 공격 
    global g
    q= deque()
    q.append((ax,ay, [(ax,ay)]))
    visited = [[0]*m for _ in range(n)]
    visited[ax][ay] = 1
    while q:
        x,y,tmp = q.popleft()
        if x == tx and y == ty:
            g[tx][ty] -= g[ax][ay]
            for r,c in tmp[1:-1]:
                g[r][c] -= (g[ax][ay]//2)
            return tmp
        for i in range(4):
            nx = (x+dx[i])%n
            ny = (y+dy[i])%m
            if not visited[nx][ny] and g[nx][ny] > 0:
                visited[nx][ny] = 1
                q.append((nx,ny, tmp+ [(nx,ny)]))
    return False# 레이저 공격을 할 수 있는 최단 경로가 없음.

def bomb():# 포탄 공격.
    global g
    g[tx][ty] -= g[ax][ay]
    tmp = []
    for i in range(8):
        nx = (tx+dx[i])%n
        ny = (ty+dy[i])%m
        if g[nx][ny] > 0 and [nx,ny] != [ax,ay]:# 대상자 주변 8방향에 공격자 제외한 칸에도 피해가 감.
            tmp.append((nx,ny))
    for x,y in tmp:
        g[x][y] -= (g[ax][ay]//2)
    tmp.append((ax,ay))
    tmp.append((tx,ty))
    return tmp# 공격과 관련된 위치 반환.

def organize(arr):# 공격과 무관하며, 부서지지 않은 포탑은 +1 증가.
    global g
    arr = set(arr)
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0 and (x,y) not in arr:
                g[x][y] += 1

for nth in range(1,k+1):# k번 반복.
    if isFinish():
        break
    ax,ay = selectAttacker()
    tx,ty = selectTarget()

    route = beam()
    if not route:
        route = bomb()
        
    organize(route)
    
answer = 0
for a in g:# 공격이 최대로 큰 값 반환.
    answer = max(answer,max(a))
print(answer)
