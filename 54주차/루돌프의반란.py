n,m,p,C,D = map(int,input().split())

rx,ry = map(int,input().split())
rx -= 1
ry -= 1

santa = [[] for _ in range(p+1)]
santaMap = [[0]*n for _ in range(n)]

for i in range(1,p+1):
    num,sx,sy = map(int,input().split())
    santa[num] = [sx-1,sy-1]
    santaMap[sx-1][sy-1] = num
point = [0]*(p+1)

sleep = [0]*(p+1)
sdx = [-1,0,1,0]# 상우하좌
sdy = [0,1,0,-1]

rdx = [-1,1,0,0,-1,-1,1,1]
rdy = [0,0,-1,1,-1,1,-1,1]

def isDone():# 모두 탈락인가.
    cnt = 0
    for i in range(1,p+1):
        x,y = santa[i]
        if [x,y] == [-1,-1]:
            cnt +=1
    if cnt == p:
        return True
    return False

def dist(x1,y1,x2,y2):
    return abs(x1-x2)**2 + abs(y1-y2)**2

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def getPoint():# 매턴 마다 탈락하지 않은 산타는 +1
    for i in range(1,p+1):
        x,y = santa[i]
        if [x,y] != [-1,-1]:
            point[i] += 1
def cascadeFromR(x,y,d,type):
    nums = []# 연쇄 반응으로 위치가 바뀔 산타번호 배열.
    locat = []# 바뀔 위치.
    while True:
        now = santaMap[x][y] # 현재 x,y에 위치한 산타 번호
        if type == 'R':# 루돌프가 움직여서 충돌 했다면.
            nx = x+rdx[d]
            ny = y+rdy[d]
        else:# 산타가 움직여서 충돌 했다면,
            nx = x+sdx[d]
            ny = y+sdy[d]
        if inRange(nx,ny):
            nums.append(now)
            locat.append((nx,ny))
            if santaMap[nx][ny] > 0:# 또 그자리에 노가 있다면,
                x,y = nx,ny
            else:
                break # 연쇄작용 끝.
        else:
            #탈락
            santa[now] = [-1,-1]
            santaMap[x][y] = 0
            break
  
    for i in range(len(nums)):
        num = nums[i]
        prevX,prevY = santa[num]# 이전 위치.
        
        nx,ny = locat[i]# 이동된 위치
        
        santa[num] = [nx,ny]
        santaMap[nx][ny] = num
    
    
def rCollsion(x,y,d):
    num = santaMap[x][y]
    point[num] += C
    nsx = x+ (rdx[d]*C)
    nsy = y + (rdy[d]*C)
  
    sleep[num] = k+2 # 충돌해서 기절. k+2번째 부터 이동 가능.
    
    if not inRange(nsx,nsy):# 겪자 밖이면 탈락.
        santaMap[x][y] = 0 #탈락
        santa[num] = [-1,-1]
    else:
        # 이동가능
        if santaMap[nsx][nsy] > 0:
            # 이동하려는 칸에 다른 산타가 있다면,
            cascadeFromR(nsx,nsy,d, 'R')
        santaMap[x][y] = 0
        santaMap[nsx][nsy] = num
        santa[num] = [nsx,nsy]
    


def closestSanta():
    cand = []
    for i in range(1,p+1):
        x,y = santa[i]
        if [x,y] != [-1,-1]:
            cand.append((dist(rx,ry,x,y), x,y))
    cand.sort(key=lambda x: (x[0], -x[1],-x[2]))
    return [cand[0][1],cand[0][2]]
def rMove():
    global rx,ry
    tx,ty = closestSanta()
    
    next = []
    for i in range(8):
        nx,ny = rx+rdx[i], ry+rdy[i]
        if inRange(nx,ny):
            next.append((dist(nx,ny,tx,ty), nx, ny, i))
    next.sort(key= lambda x: x[0])
    rx,ry = next[0][1],next[0][2]
    
    nd = next[0][3]
    

    if santaMap[rx][ry] > 0: #충돌이라면
    
        rCollsion(rx,ry,nd)

def sCollision(x,y,d):
    num = santaMap[x][y]
    point[num] += D
    nsx = x+(sdx[d]*D)
    nsy = y+(sdy[d]*D)
    
    sleep[num] = k+2 
    
    if not inRange(nsx,nsy):
        santaMap[x][y] = 0
        santa[num] = [-1,-1]# 탈ㄹㅏㄱ
    else:
        # 이동가능
        if santaMap[nsx][nsy] > 0:
            cascadeFromR(nsx,nsy,d,'S')
        santaMap[x][y] = 0
        santaMap[nsx][nsy] = num
        santa[num] = [nsx,nsy]

def sMove():
    for i in range(1,p+1):
        if sleep[i] <= k and santa[i] != [-1,-1]:
           
            cand = []
            x,y = santa[i]
            prev = dist(rx,ry,x,y)
            
            for j in range(4):
                nx,ny = x+sdx[j],y+sdy[j]
                if inRange(nx,ny) and santaMap[nx][ny] == 0:
                    next = dist(rx,ry,nx,ny)
                    if next < prev:
                        cand.append((next, nx,ny, j))
            if len(cand) == 0:
                continue
            else:
                
                cand.sort(key =lambda x:(x[0], x[3]))# 가장 가깝고, 상우하좌 우선순위
                nx,ny = cand[0][1],cand[0][2]
                santa[i] = [nx,ny]
                santaMap[x][y] = 0
                santaMap[nx][ny] = i
                nd = cand[0][3] # 이동한 방향.
                if [rx,ry] == [nx,ny]:# 충돌. 이때는 이동방향의 반대방향 으로 이동해야함.
                    sCollision(nx,ny,(nd+2)%4)

            
for k in range(1,m+1):   
    if isDone():
        break
    rMove()
    sMove()
    getPoint()
  
for i in range(1,p+1):
    print(point[i],end=' ')

