from collections import deque
n,m,p,C,D = map(int,input().split())
rx,ry = map(int,input().split())
rx -= 1
ry -=1
g = [[[] for _ in range(n)] for _ in range(n)]
santa = {}
sleep= {}
dx = [-1,0,1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,-1,1]

point = [0]*(p+1)
cnt = p
for _ in range(p):
    num,x,y = map(int,input().split())
    santa[num] = [x-1,y-1]
    sleep[num] =0
    g[x-1][y-1].append(num)

def givePoint():
    global point
    for num in santa:
        point[num] += 1
def isFinish():
    return cnt <=0

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def getDist(x1,y1,x2,y2):
    return abs(x1-x2)**2 + abs(y1-y2) ** 2

def cascading(x,y,di):# 상호 작용 발생.
    global g,santa, cnt
    arr =[]# 그 다음 이동할 위치를 저장
    q= deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        nx = x+dx[di]
        ny = y+dy[di]
        if inRange(nx,ny):
            arr.append((g[x][y][0],nx,ny))
            g[x][y].pop()
            if len(g[nx][ny]) > 0:
                q.append((nx,ny))
        else:
            # 바로 탈락.
            number = g[x][y][0]
            g[x][y].pop()
            del santa[number]
            cnt -= 1
    for number,nx,ny in arr:
        santa[number] = [nx,ny]
        g[nx][ny].append(number)

def collision(number,score,di):
    global sleep,cnt,g,santa
    sleep[number] = nth+2# 충돌이후 기절
    point[number] += score# 점수 획득.
    x,y = santa[number]
    nx = x+(dx[di]*score)# 방향대로 C orD 칸 밀림.
    ny = y+(dy[di]*score)
    if not inRange(nx,ny):
        g[x][y].pop()
        del santa[number]
        cnt -= 1
    else:
        if len(g[nx][ny]) > 0:# 충돌 후, 밀린 칸에 다른 산타가 있다면, 상호작용 발생.
            cascading(nx,ny,di)
        # 상호작용 이후, 또는 상호작용이 일어나지 않는다면. 밀린 산타 위치 이동.
        g[x][y].pop()
        g[nx][ny].append(number)
        santa[number] = [nx,ny]


def santaMove(number):# 산타 이동.
    global g,santa
    x,y = santa[number]
    cand = []
    for i in range(4):
        nx  = x+dx[i]
        ny = y+dy[i]
        if inRange(nx,ny) and len(g[nx][ny]) == 0:
            dist1 = getDist(rx,ry,nx,ny)
            dist2 = getDist(rx,ry,x,y)
            if dist1 < dist2:
                cand.append((dist1,i))
    if len(cand) > 0:
        cand.sort(key=lambda x:(x[0],x[1]))
        _,nd = cand[0]
        nx = x+dx[nd]
        ny = y+dy[nd]
        santa[number] = [nx,ny]
        g[x][y].pop()
        g[nx][ny].append(number)
        if nx == rx and ny == ry:# 이동 이후 루돌프와 충돌 했다면,
            collision(number,D,(nd+2)%4)
def ruMove():# 루돌프 이동.
    global rx,ry
    cand = []
    for num in santa:
        x,y = santa[num]
        dist = getDist(x,y,rx,ry)
        cand.append((dist,x,y))
    cand.sort(key=lambda x:(x[0],-x[1],-x[2]))
    tx,ty = cand[0][1],cand[0][2]
    cand = []
    for i in range(8):
        nx = rx+dx[i]
        ny = ry+dy[i]
        if inRange(nx,ny):
            dist = getDist(nx,ny,tx,ty)
            cand.append((dist,i,nx,ny))
    cand.sort(key=lambda x:x[0])
    _, nd,nx,ny = cand[0]
    rx,ry = nx,ny
    
    if len(g[rx][ry]) > 0:# 이동 이후, 해당 칸에 산타가 존재한다면, 충돌 발생.
        number = g[rx][ry][0]
        collision(number,C,nd)
for nth in range(1,m+1):

    ruMove()
   
    for num in range(1,p+1):
        if num in santa and sleep[num] <= nth:
            santaMove(num)
            
    if isFinish():
        break
    givePoint()


for i in range(1,p+1):
    print(point[i],end= ' ')