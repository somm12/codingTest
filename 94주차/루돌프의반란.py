from collections import deque
n,m,p,C,D = map(int,input().split())

rx,ry = map(int,input().split())
rx -= 1
ry -= 1

santa = {}
sInfo = [[0]*n for _ in range(n)]
score = [0]*(p+1)

dx = [-1,0,1,0,-1,-1,1,1]# 상 우 하 좌. 대각선 ( 루돌의 8방향. 산타 4방향 같이 쓰는 방향 배열)
dy = [0,1,0,-1,-1,1,1,-1]

for _ in range(p):
    numb,x,y = map(int,input().split())
    santa[numb] = [x-1,y-1,0]
    sInfo[x-1][y-1]= numb


def getDist(a,b,c,d,):# 거리 계산 기준.
    return (a-c)**2 + (b-d)**2
def inRange(x,y):
    return 0 <= x< n and 0 <= y < n
# 상호 작용.
def go(x,y,d):
    global santa
    diff = []
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        nb = sInfo[x][y]
        diff.append(nb)
        nx,ny= x+dx[d],y+dy[d]
        if not inRange(nx,ny):
            continue
        else:
            if sInfo[nx][ny] > 0:
                q.append((nx,ny))
    for nb in diff:
        x,y,_ = santa[nb]
        nx,ny = x+dx[d],y+dy[d]
        if inRange(nx,ny):
            santa[nb][0],santa[nb][1] = nx,ny
            sInfo[nx][ny] = nb
        else:
            del santa[nb]

# 충돌.
def collision(x,y,d,point):
    global score,santa,sInfo
    number = sInfo[x][y]
    score[number] += point
    santa[number][2] = nth+2
    sInfo[x][y] = 0
    nx,ny = x + (dx[d]*point), y + (dy[d]*point)
    if not inRange(nx,ny):
        del santa[number]
    else:
        if sInfo[nx][ny] > 0:
            go(nx,ny,d)
        santa[number][0],santa[number][1] = nx,ny
        sInfo[nx][ny] = number
# 산타 이동.
def sMove(num):
    global santa,sInfo
    sx,sy,_ = santa[num]
    cand = []
    for i in range(4):
        nx,ny = sx+dx[i],sy+dy[i]
        if inRange(nx,ny) and sInfo[nx][ny] == 0:
            prev = getDist(sx,sy,rx,ry)
            nxt = getDist(nx,ny,rx,ry)
            if nxt < prev:
                cand.append((nxt,i))
    if len(cand) != 0:
        cand.sort(key =lambda  x: (x[0],x[1]))
        nd = cand[0][1]
        nx,ny = sx+dx[nd],sy+dy[nd]
        santa[num][0],santa[num][1] = nx,ny
        sInfo[sx][sy] = 0
        sInfo[nx][ny] = num
        if nx == rx and ny == ry:# 루돌프와 충돌 .
            collision(nx,ny,(nd+2)%4, D)
# 루돌프 이동.
def rMove():
    global rx,ry
    cand = []
    for i in santa:
        sx,sy,_ = santa[i]
        dist = getDist(rx,ry,sx,sy)
        cand.append((dist,sx,sy))
    cand.sort(key = lambda x : (x[0], -x[1],-x[2]))
    tx,ty = cand[0][1],cand[0][2]

    cand = []
    for i in range(8):
        nx,ny = rx + dx[i],ry + dy[i]
        if inRange(nx,ny):
            dist = getDist(nx,ny,tx,ty)
            cand.append((dist,nx,ny,i))
    cand.sort(key=lambda x: x[0])
    _,rx,ry,nd = cand[0]
    if sInfo[rx][ry] > 0:
        collision(rx,ry,nd,C)


for nth in range(1,m+1):
    rMove()
    for num in range(1,p+1):
        if num not in santa or santa[num][2] > nth:# 산타가 탈락 or 기절 중이면 넘기기
            continue
        sMove(num)
  
    if len(santa) == 0:
        break
    for i in santa:
        score[i] += 1

for i in range(1,p+1):
    print(score[i],end=' ')
# 코드트리 루돌프의반란.