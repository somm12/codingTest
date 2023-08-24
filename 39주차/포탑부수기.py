from collections import deque
dx = [0,1,0,-1]# 우하좌상 방향 우선으로 레이저 공격에서 최단 경로를 찾는다.
dy = [1,0,-1,0]

mx = [-1,-1,0,1,1,1,0,-1]# 포탄 공격에서 주변 8가지 방향으로 포탄을 던짐.
my = [0,1,1,1,0,-1,-1,-1]

n,m,k = map(int,input().split())
record = [[0]*m for _ in range(n)]# 공격자, 공격 대상자 선정 때 최근 공격 시점을 알기 위한 배열.
g = []

for _ in range(n):
    g.append(list(map(int,input().split())))
answer = -1

def isFinish():# 남은 포탑이 1개라면 True
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] > 0:
                cnt += 1
    if cnt == 1:
        return True
    return False

def attacker():# 공격자 선정. 
    # 부서지지않은 포탑 중에서, 공격력이 작고, 가장 최근에 공격, 행과 열 합이 크고, 열이 큰 순서.
    global record, g
    cand = []
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                cand.append((g[x][y], record[x][y], x+y,x,y)) 
    cand.sort(key=lambda x:(x[0], -x[1], -x[2], -x[4]))
    x,y = cand[0][3],cand[0][4]
    record[x][y] = nth# 최근 공격 시점 할당.
    g[x][y] += (n+m)# 공격력 n+m 증가.

    return [x,y]

def target():# 공격 대상자 선정.
    # 공격력이 가장 크고, 가장 오래전에 공격했으며, 행과 열 합이 작고, 열이 작은 순서 정렬.
    cand = []
    for x in range(n):
        for y in range(m):# 공격자 제외, 부서지지 않은 포탑 중에서
            if g[x][y] > 0 and not (x== ax and y == ay):
                cand.append((g[x][y], record[x][y], x+y,x,y))
    
    cand.sort(key=lambda x:(-x[0], x[1], x[2], x[4]))
    x,y = cand[0][3],cand[0][4]
    return [x,y]

def beam():# 레이저 공격 수행.
    # 범위를 벗어나도 행끼리, 열끼리 이어짐.
    q= deque()
    q.append((ax,ay, []))# 시작점과, 최단 경로의 좌표들을 담는다.
    visited = [[0]*m for _ in range(n)]# 방문 처리.

    visited[ax][ay] = 1
    while q:
        x,y, route = q.popleft()
        if x == tx and y == ty:# 공격 대상 만나면 최단 경로 route 반환
            return route
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nx %= n  # 범위를 벗어나도 행끼리, 열끼리 이어짐.
            ny %= m
            if not visited[nx][ny] and g[nx][ny] > 0:# 무너지지 않은 포탑으로 이동 가능.
                visited[nx][ny] = 1
                q.append((nx,ny, route+[(nx,ny)])) # 현재까지의 경로에 추가한 경로를 append
    return False # 만약 공격 대상에 도달을 못하면 False

def breamAttack(route):# 레이저 공격 수행
    global g
    g[tx][ty] -= g[ax][ay]
    tmp = g[ax][ay]//2# 경로에 해당하는 위치의 포탑은 공격력의 반만큼 피해를 본다.

    for x,y in route:
        if not (tx == x and ty == y):# 공격자가 경로에 포함되어서 제외 시킨다.
            g[x][y] -= tmp

def throw():# 포탄 공격.
    global g
    arr = []# 공격 당하는 좌표 넣기. 정비할 때 공격 관련 부분을 알기 위해서.
    g[tx][ty] -= g[ax][ay]

    tmp = g[ax][ay]//2# 공격 대상 제외, 주변 8방향 위치는 절반 만큼만 손해

    for i in range(8):
        nx = (tx+mx[i]) % n # 범위 벗어나도 행. 열 끼리 이어짐.
        ny = (ty+my[i]) % m
        if not (nx == ax and ny == ay): # 공격자를 제외하고 주변 8방향 공격.
            if g[nx][ny] > 0:
                g[nx][ny] -= tmp
                arr.append((nx,ny)) 
    return arr# 정비를 위해서 공격 받은 위치 배열 반환.

def arrange(route):# 정비하는 함수, route로 공격 관련 위치 좌표를 받아옴.
    global g
    exception = {}# 제외할 모든 좌표를 담을 딕셔너리.

    for x,y in route:
        exception[(x,y)] = 1
    # 공격자, 공격대상자 도 제외.
    exception[(tx,ty)] = 1
    exception[(ax,ay)] = 1 

    for x in range(n):
        for y in range(m):
            # 무너지지 않은 포탑 중에서, 공격과 관련 없는 위치는 공격력 +1.
            if (x,y) not in exception and g[x][y] >0:
                g[x][y] += 1


for nth in range(1,k+1):
    if isFinish():# 남은 포탑이 1개라면 즉시 종료.
        break
    ax,ay = attacker()# 공격자 선정

    tx,ty = target()# 공격 대상자 선정
    route = beam() # 레이저 공격
    if route == False:# 레이저 공격이 불가능이면
        route = throw() # 포탄 공격
        
    else:
        breamAttack(route) # 해당 route에 레이저 공격 진행.
    
    arrange(route) # 정비.
    

for x in range(n):# 포탑 최대 공격력 구하기.
    for y in range(m):
        answer = max(answer,g[x][y])
print(answer)
# 코드 트리 삼성 기출