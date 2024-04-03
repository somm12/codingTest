from collections import deque

n,m,p,C,D = map(int,input().split())
rx,ry = map(int,input().split())
rx -= 1
ry -= 1
g = [[[] for _ in range(n)] for _ in range(n)]# 칸에 산타 번호를 담을 격자
santa = {}# 산타번호 : 산타의 위치 정보를 담을 딕셔너리.

dx = [-1,0,1,0, 1,1,-1,-1]# 상 우 하 좌(산타 이동시 우선 순위) + 나머지 대각선 방향.
dy = [0,1,0,-1, 1,-1,-1,1]

for _ in range(p):
    num,x,y = map(int,input().split())
    santa[num] = [x-1,y-1]
    g[x-1][y-1].append(num)

point = [0]*(p+1)# 점수
slept = [0]*(p+1)# 잠들었는지 체크해두는 배열.

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def getDist(x,y,a,b):# 두점 사이의 거리.
    return abs(x-a)**2 + abs(y-b)**2

def cascading(x,y,di):# x,y 위치에서 di방향으로 연쇄이동 처리 함수.
    global g, santa

    q = deque()
    santaNum = g[x][y][0]
    q.append((x,y,santaNum))
    ntx = []# 다음 이동할 위치를 담을 배열

    while q:
        x,y,number = q.popleft()
        nx,ny = x+dx[di],y+dy[di]
        if not inRange(nx,ny):# 만약 격자판을 벗어난다면, 삭제.
            g[x][y].pop()
            del santa[number]
        else:
            g[x][y].pop()
            ntx.append((nx,ny,number))
            if len(g[nx][ny]) > 0:
                q.append((nx,ny, g[nx][ny][0]))
    for x,y,number in ntx:
        g[x][y].append(number)
        santa[number] = [x,y]


def collision(x,y,score,di):# x,y 위치에서 di방향으로 이동하는 충돌. score 만큼 점수 획득, score만큼 이동.
    global santa, g, point, slept
    santaNum = g[x][y][0]
    slept[santaNum] = nth+2 # 현재턴+2 부터 이동 가능. 그 전까지 기절.

    point[santaNum] += score

    nx = x+ (dx[di] * score)
    ny = y + (dy[di]* score)
    if not inRange(nx,ny):
        del santa[santaNum]
        g[x][y].pop()
    else:
        g[x][y].pop()
        if len(g[nx][ny]) > 0:#다른 산타가 있다면, 연쇄 이동 시작.
            cascading(nx,ny,di)
        g[nx][ny].append(santaNum)
        santa[santaNum] = [nx,ny]

def santaMove(number):# 산타 이동.
    global santa,g
    x,y = santa[number]
    cand = []
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if inRange(nx,ny) and len(g[nx][ny]) == 0:
            dist1= getDist(rx,ry,nx,ny)
            dist2 = getDist(rx,ry,x,y)
            if dist1 < dist2:# 더 가까워지는 이동 가능 방향으로만 이동.
                cand.append((dist1,i))
    if len(cand) > 0:
        cand.sort(key= lambda x:(x[0],x[1]))
        nd = cand[0][1]
        nx,ny = x+dx[nd],y+dy[nd]
        santa[number] = [nx,ny]
        g[x][y].pop()
        g[nx][ny].append(number)
        if rx == nx and ry == ny:# 이동한 방향에 루돌프가 있다면, 충돌. 단, 충돌시, 반대 방향으로 이동하게 됨.
            collision(nx,ny,D, (nd+2) % 4)

def ruMove():# 루돌프 이동.
    global rx,ry
    cand = []
    for num in santa:
        x,y = santa[num]
        dist = getDist(x,y,rx,ry)
        cand.append((dist,x,y))
    cand.sort(key=lambda x:(x[0],-x[1],-x[2]))# 가장 가깝고, 행이 크고 열이 큰 산타를 대상으로 정함.
    tx,ty = cand[0][1],cand[0][2]
    cand = []
    for i in range(8):
        nx = rx+dx[i]
        ny = ry+dy[i]
        if inRange(nx,ny):
            dist = getDist(tx,ty,nx,ny)
            cand.append((dist,nx,ny,i))
    cand.sort(key=lambda x:x[0])# 8방향 중 해당 산타와 가장 가까워지는 방향으로 이동.
    _, rx,ry, nd = cand[0]

    if len(g[rx][ry]) > 0:# 해당 칸에 산타가 있다면 충돌.
        collision(rx,ry, C, nd)

def isDone():# 산타가 모두 탈락 되었다면, 종료. 살아남은 산타는 모두 +1 획득.
    global point
    if len(santa) == 0:
        return True

    for number in santa:
        point[number] += 1
    return False

for nth in range(1,m+1):
    ruMove()
    for num in range(1,p+1):
        if num in santa and slept[num] <= nth:# 산타가 탈락되지 않았으면서, 기절하지 않은 산타만 이동.
            santaMove(num)
        
    if isDone():
        break

for i in range(1,p+1):
    print(point[i],end=' ')