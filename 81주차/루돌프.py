from collections import deque
n,m,p,C,D =map(int,input().split())
rx,ry = map(int,input().split())
rx-= 1
ry -= 1
santa = {}
locat = [[0]*n for _ in range(n)]
for _ in range(p):
    num,x,y = map(int,input().split())
    santa[num] = [x-1,y-1,0]
    locat[x-1][y-1] = num
dx = [-1,0,1,0]
dy = [0,1,0,-1]
point = [0]*(p+1)
rdx = [-1,0,1,0,-1,-1,1,1]
rdy = [0,1,0,-1,1,-1,1,-1]

def inRange(x,y):
    return 0 <= x< n and 0 <= y < n
def getDist(x,y,a,b):
    return abs(x-a)**2 + abs(y-b)**2

def rMove():
    global rx,ry
    cand = []
    for num in santa:
        x,y,_ = santa[num]
        dist = getDist(x,y,rx,ry)
        cand.append((dist,x,y))
    cand.sort(key= lambda x:(x[0],-x[1],-x[2]))
    # 목표로하는 산타 번호.
    tx,ty = cand[0][1],cand[0][2]
    tNum = locat[tx][ty]
    # 방향 정하기
    cand =[]
    for i in range(8):
        nx = rx+rdx[i]
        ny = ry+rdy[i]
        dist = getDist(nx,ny,tx,ty)
        if inRange(nx,ny):
            cand.append((dist,nx,ny,i))
    cand.sort(key= lambda x:x[0])
    rx,ry = cand[0][1],cand[0][2]
    nd = cand[0][3]
    if locat[rx][ry] > 0:# 산타와 충돌.
        sNum = locat[rx][ry]
        collision(C,nd,sNum)

def sMove(num):
    global santa,locat
    x,y,_ = santa[num]
    pDist = getDist(x,y,rx,ry)

    cand = []
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if inRange(nx,ny) and locat[nx][ny] == 0:
            nDist = getDist(nx,ny,rx,ry)
            if nDist < pDist:
                cand.append((nDist, nx,ny,i))

    if len(cand) != 0:# 이동할 수 있는 칸이 있다면.
        cand.sort(key = lambda x: x[0])
        _,nx,ny,nd = cand[0]
        locat[x][y] = 0
        santa[num][0],santa[num][1] = nx,ny
        if nx == rx and ny == ry:# 충돌.
            collision(D,(nd+2)%4,num)

        else:# 루돌프 없음.
            santa[num][0],santa[num][1] = nx,ny
            locat[x][y] = 0
            locat[nx][ny] = num

def push(x,y,di):
    global santa,locat
    q= deque()
    q.append((x,y))
    ret = []# 산타 번호와 다음 이동할 위치.
    while q:
        x,y = q.popleft()
        nx,ny= x+rdx[di],y+rdy[di]
        if not inRange(nx,ny):
            sNum = locat[x][y]
            del santa[sNum]
            break
        if locat[nx][ny] > 0:
            q.append((nx,ny))
        ret.append((locat[x][y], nx,ny))

    for sNum,nx,ny in ret:
        santa[sNum][0],santa[sNum][1] = nx,ny
        locat[nx][ny] = sNum

def collision(score,direct,sNum):
    global point, santa, locat
    point[sNum] += score
    x,y,_ = santa[sNum]
    nx,ny = x+ (rdx[direct]*score), y + (rdy[direct]*score)
    if not inRange(nx,ny):
        del santa[sNum]
        locat[x][y] = 0
    else:
        if locat[nx][ny] > 0 and sNum != locat[nx][ny]:
            push(nx,ny,direct)
        santa[sNum] = [nx,ny,t+1]# 충돌했으니 기절.
        locat[x][y] = 0
        locat[nx][ny] = sNum


for t in range(1,m+1):
    if len(santa) == 0: break
    rMove()

    for num in range(1,p+1):

        if num not in santa or t <= santa[num][2]: continue
        sMove(num)
    for num in range(1,p+1):
        if num in santa:
            point[num] += 1
for i in range(1,p+1):
    print(point[i],end=' ')
# 코드트리 루돌프의 반란 