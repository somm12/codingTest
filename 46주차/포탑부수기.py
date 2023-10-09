from collections import deque

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer =0

dx = [0,1,0,-1]
dy = [1,0,-1,0]# 우 하 좌 상
mx = [-1,-1,0,1,1,1,0,-1]
my = [0,1,1,1,0,-1,-1,-1]
lastAttack = [[0]*m for _ in range(n)]


def attacker():
    cand = []# 후보들
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cand.append((g[x][y], lastAttack[x][y],x+y,x,y))
    cand.sort(key =lambda x:(x[0], -x[1], -x[2], -x[4]))
    i,j = cand[0][3],cand[0][4]
    return [i,j]

def target():
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y]>0 and [ax,ay] != [x,y]:
                cand.append((g[x][y], lastAttack[x][y],x+y,x,y))
    cand.sort(key =lambda x:(-x[0], x[1], x[2], x[4]))
    i,j = cand[0][3],cand[0][4]
    return [i,j]

def beem():
    global g,lastAttack, related
    q = deque()
    q.append((ax,ay,[(ax,ay)]))

    visited = [[0]*m for _ in range(n)]
    visited[ax][ay] = 1
    while q:
        x,y,route = q.popleft()

        if x == tx and y == ty:

            value = g[ax][ay]
            g[tx][ty] -= value
            lastAttack[ax][ay] = nth
            for a,b in route:
                related[a][b]=1
            route = route[1:-1]
            for a,b in route:
                g[a][b] -= (value//2)

            return True

        for i in range(4):
            nx = (x+dx[i])%n
            ny = (y+dy[i])%m
            if g[nx][ny] > 0 and not visited[nx][ny] :
                q.append((nx,ny, route + [(nx,ny)]))
                visited[nx][ny] =1
    return False

def throw():
    global g,lastAttack, related
    value = g[ax][ay]
    g[tx][ty] -= value
    related[ax][ay], related[tx][ty] = 1,1
    lastAttack[ax][ay] = nth
    for i in range(8):
        nx = (tx+mx[i]) % n
        ny = (ty+my[i]) % m

        if g[nx][ny] >0 and [nx,ny] != [ax,ay]:
            g[nx][ny] -= (value//2)
            related[nx][ny] =1

def isAllCrash():
    cnt =0
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cnt += 1
    return cnt == 1

def org():
    global g
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0 and not related[x][y]:
                g[x][y] +=1


for nth in range(1,k+1):


    related = [[0]*m for _ in range(n)]
    ax,ay = attacker()
    g[ax][ay] += (n+m)
    tx,ty = target()



    if not beem():# 레이저 공격 시도
        throw()# 안돼면 포탄 던지기 공격을 하기

    if isAllCrash():# 1개 빼고 다 부서 졌다면 즉시 종료
        break

    org()# 정비하기. 공격과 무관했던, 부서서지 않은 포탑들은 +1


for x in range(n):
    for y in range(m):
        answer = max(answer,g[x][y])
print(answer)

