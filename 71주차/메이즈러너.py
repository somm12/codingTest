n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
player = {}
for num in range(1,m+1):
    x,y = map(int,input().split())
    player[num] = [x-1,y-1]
ex,ey = map(int,input().split())
ex -= 1
ey -= 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def getDist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move():
    global player,answer
    tmp = {}
    for num in player:
        x,y = player[num]
        cand = []
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and g[nx][ny] == 0:
                dist1 = getDist(x,y,ex,ey)
                dist2 = getDist(nx,ny,ex,ey)
                if dist2 < dist1:# 이동했을 때, 출구와의 거리가 더 짧아야함.
                    cand.append((nx,ny,i))
        if len(cand) == 0:#그대로
            tmp[num] = [x,y]
        else:
            cand.sort(key=lambda x:x[2])
            answer += 1
            nx,ny,_ = cand[0]
            if nx == ex and ny == ey:# 이동 후, 탈출구에 도착하면 즉시 탈출.
                continue
            else:
                tmp[num] = [nx,ny]
    player = tmp

def isFinish():
    return len(player) == 0

def check(sx,sy,length):
    isExit = False
    isPeople = False
    if sx <= ex < sx + length and sy <= ey < sy+length:
        isExit = True
    for num in player:
        a,b = player[num]
        if sx <= a < sx+length and sy <= b < sy+length:
            isPeople = True
            break
    return isExit and isPeople

def rotate(sx,sy,length):
    global g,player, ex,ey
    newG = [arr[:] for arr in g]
    tmp = {}

    for x in range(length):
        for y in range(length):
            px = sx+x # 이전 위치
            py = sy+y
            nx = sx+y # 바뀌는 위치.
            ny = sy + length - 1 - x
            if g[px][py] > 0:# 내구도 -1 
                newG[nx][ny] = g[px][py] - 1
            else:
                newG[nx][ny] = g[px][py]
    # 탈출구 회전.
    ex -= sx# 0,0 쪽으로 끌어올린다.
    ey -= sy
    nx,ny = ey, length - 1 - ex
    ex,ey = sx+nx,sy+ny
    # 참가자들 회전.
    for num in player:
        x,y = player[num]
        if sx <= x< sx+length and sy <= y < sy+length:
            x -= sx
            y -= sy
            nx,ny = y,length - 1 -x
            tmp[num] = [nx+sx,ny+sy]
        else:# 회전 범위가 아닌 참가자는 그대로.
            tmp[num] = [x,y]

    player = tmp
    g = newG


def smallSquare():
    for length in range(2,n+1):# 가장 작고, 행이 작고, 열이 작은 우선선위.
        for r in range(n):
            for c in range(n):# 그 중에서 참가자 1명 이상, 탈출구 포함 회전.
                if r + length <= n and c + length <= n and check(r,c,length):
                    return [r,c,length]

answer = 0
for nth in range(1,k+1):
    
    move()# 이동
   
    if isFinish():# 모두 탈출했는지 확인.
        break
    sx,sy,length = smallSquare()# 가장 작은 정사각형 찾기.
   
    rotate(sx,sy,length)# 회전.
    

print(answer)
print(ex+1,ey+1)