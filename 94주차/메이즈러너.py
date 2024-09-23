n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
p = {}
for i in range(1,m+1):
    x,y = map(int,input().split())
    p[i] = [x-1,y-1]
ex,ey = map(int,input().split())
ex -= 1
ey -=1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def inRange(x,y):
    return 0<=x< n and 0<=y <n

def move():
    global p,answer
    tmp = {}
    for num in p:
        x,y= p[num]
        cand = []
        prev = abs(x-ex) + abs(y-ey)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            nxt = abs(nx-ex) + abs(ny-ey)
            if inRange(nx,ny) and g[nx][ny] == 0 and nxt < prev:# 빈칸이며, 탈출구와 더 가까워져야함.
                cand.append((nx,ny))# dx,dy가 상하좌우 이므로, 만약 가능한 이동할 칸이면 바로, cut 시키기.
                break
        if len(cand)> 0:
            nx,ny = cand[0]
            answer += 1
            if not (ex == nx and ey == ny):
                tmp[num] = [nx,ny]
        else:# 이동을 못하는 경우는 그대로 위치를 반영.
            tmp[num] = [x,y]
    p = tmp

def square():
    for L in range(2,n+1):
        for sx in range(n):
            for sy in range(n):
                # 범위를 벗어나지 않고, 조건에 맞는지 확인
                if sx + L <= n and sy + L <= n and check(sx,sy,L):
                    return [sx,sy,L]
def check(sx,sy,L):# 해당 범위내에 한 명이상의 참여좌와 탈출구가 있는지 확인.
    flag = False
    if sx <= ex < sx+L and sy <= ey < sy+L:
        flag = True

    cnt =0
    for num in p:
        x,y = p[num]
        if (sx <= x < sx+L and sy <= y < sy+L):
            cnt += 1
            break
    return cnt >= 1 and flag

def rotate(sx,sy,L):
    global g,p,ex,ey

    np = {}
    nex,ney =0,0
    tmp = [v[:] for v in g]
    for x in range(L):
        for y in range(L):
            px,py = sx+ x,sy+ y
            nx,ny = sx+ y, sy + L-1-x
            if g[px][py] > 0:# 벽이 있는 칸이면 -1.
                tmp[nx][ny] = g[px][py] -1
            else:
                tmp[nx][ny] = g[px][py]
                if ex == px and ey == py:# 탈출구도 회전.
                    nex,ney = nx,ny
                for num in p:# 참여자도 회전.
                    mx,my = p[num]
                    if mx == px and my == py:
                        np[num] = [nx,ny]
    for num in p:# 정사각형 범위 밖에 있는 참여자들은 위치가 그대로 이므로, 반영하기.
        x,y = p[num]
        if num not in np:
            np[num] = [x,y]
    ex,ey = nex,ney
    p = np
    g = tmp

answer = 0
for nth in range(1,k+1):
    move()

    if len(p) == 0:# 참가자가 모두 탈출시, 게임 종료.
        break
    sx,sy,L = square()# 시작점 좌상단 sx,sy, 정사각형의 길이 L
    rotate(sx,sy,L)# 회전.
print(answer)
print(ex+1,ey+1)
# 코드트리 메이즈러너 문제


