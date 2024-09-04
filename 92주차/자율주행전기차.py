from collections import deque

n,m,fuel = map(int,input().split())
g =[]
for _ in range(n):
    g.append(list(map(int,input().split())))

cx,cy= map(int,input().split())
cx -= 1
cy -= 1
p ={}
for _ in range(m):
    a,b,c,d = map(int,input().split())
    p[(a-1,b-1)]=[c-1,d-1]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def select():
    q= deque()
    q.append((cx,cy,0))
    cand = []
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    while q:
        x,y,dist = q.popleft()
        if (x,y) in p:
            cand.append((x,y,dist))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 0:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = 1
    if len(cand)>0:
        cand.sort(key=lambda x: (x[2],x[0],x[1]))
        return cand[0]
    return False

def pickUp():
    global fuel, cx,cy
    fuel -= need
    cx,cy = tx,ty

def go():
    q= deque()
    ex,ey = p[(tx,ty)]
    q.append((0,cx,cy))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    while q:
        dist,x,y= q.popleft()
        if x == ex and y== ey:
            return dist
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((dist+1,nx,ny))
    return False # 목적지 이동 불가

flag = True
while len(p) > 0:
    info = select()
    if info == False:# 모실 수 있는 승객이 없음.
        flag = False
        break
    tx,ty,need = info

    if fuel < need:# 픽업 도중 연료 소진.
        flag= False
        break

    pickUp()# 승객 태우기. 택시 이동. 연료 소진
    need = go()# 목적지까지 이동.
    if need == False or need > fuel:# 목적지에 접근 불가 or 도중에 연료 소진.
        flag = False
        break
    else:# 무사히 잘 도착.
        fuel += need# 연료 충전
        ncx,ncy = p[(tx,ty)]
        cx,cy = ncx,ncy# 택시 이동
        del p[(tx,ty)]# 도착했으므로, p에서 승객 삭제.
if flag:
    print(fuel)
else:
    print(-1)
# 코드트리 자율주행 전기차.