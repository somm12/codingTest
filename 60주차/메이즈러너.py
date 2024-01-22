n,m,k = map(int,input().split())
g = []
people = {}
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    g.append(list(map(int,input().split())))
for i in range(1,m+1):
    x,y = map(int,input().split())
    people[i] = [x-1,y-1]
ex,ey = map(int,input().split())
ex -= 1
ey -= 1

def square():# 가장 작은 정사각형 찾기.
    for L in range(2,n+1):
        for x in range(n):
            for y in range(n):
                if inRange(x+L-1,y+L-1):
                    pFlag = False
                    eFlag = False
                    for num in people:
                        a,b = people[num]
                        if x <= a < x+L and y <= b < y+L:
                            pFlag = True
                    if x <= ex < x+L and y <= ey < y+L:
                        eFlag = True
                    if eFlag and pFlag:
                        return [x,y,L]


def rotate():# 회전
    global people, ex,ey,g
    newG = [[0]*n for _ in range(n)]
    tmp = {}
    for x in range(n):
        for y in range(n):
            newG[x][y] = g[x][y]
    sx,sy,L = square()
    
    for x in range(sx,sx+L):
        for y in range(sy,sy+L):
            newG[x][y] = 0
    flag = True# 출구 위치 변화 여부.
    for x in range(L):
        for y in range(L):
            px,py = sx+x,sy+y# 이전 좌표
            nx,ny = sx+y, sy+ L-1-x# 회전 후 좌표
            if g[px][py] > 0:
                g[px][py] -= 1# 내구성 -1
            newG[nx][ny] = g[px][py]
            if [px,py] == [ex,ey] and flag:# 탈출구 바뀜.
                flag = False
                ex,ey = nx,ny
            for num in people:
                a,b = people[num]
                if [a,b] == [px,py]:
                    tmp[num] = [nx,ny]
    for num in people:
        if num not in tmp:
            x,y = people[num]
            tmp[num] = [x,y]
    g = newG
    people = tmp
def move():# 이동.
    global people, answer
    tmp = {}
    for num in people:
        x,y = people[num]
        prevDist = abs(x-ex)+abs(y-ey)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] == 0:
                nDist = abs(nx-ex)+abs(ny-ey)
                if nDist < prevDist:
                    answer += 1
                    if [nx,ny] == [ex,ey]:# 출구로 이동하면 tmp에 좌표 넣기 않기(참여자 0명되면 종료.)
                        break
                    else:
                        tmp[num] = [nx,ny]
                        break
        else:# 이동할 곳이 없다면 그대로.
            tmp[num] = [x,y]
    people = tmp

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

for t in range(k):
    move()
    if len(people) == 0:# 이동 후 모두 탈출했다면 종료.
        break
    
    rotate()
    
print(answer)
print(ex+1,ey+1)

