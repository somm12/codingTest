from collections import deque

n,m,battery = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

cx,cy = map(int,input().split())# 차 위치
cx -= 1
cy -=1

p = {}

for _ in range(m):# 사람들의 위치와 목적지 위치를 담은 딕셔녀리 할당.
    a,b,c,d = map(int,input().split())
    p[(a-1,b-1)] = [c-1,d-1]

dx =[-1,1,0,0]
dy = [0,0,-1,1]
def choose():# 가장 가까운 거리에 있는 승객 찾기.
    cand = []
    q= deque()
    q.append((cx,cy,0))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    while q:
        x,y,cnt = q.popleft()
        if (x,y) in p:
            cand.append((cnt,x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 0:
                q.append((nx,ny,cnt+1))
                visited[nx][ny]=1
    if len(cand) == len(p):# 만약 한 명이라도 태울 수 없는 경우라면, False 반환.
        cand.sort(key=lambda x:(x[0],x[1],x[2]))# 가깝고, 행과 열이 작은 순서
        cnt,x,y = cand[0]
        return [x,y,cnt]
    return False

def pickUp(x,y,dist):# 승객 태우기
    global cx,cy,battery
    if battery < dist:# 배터리 양이 거리보다 적다면, 즉시 종료.
        return False
    battery -= dist
    cx,cy = x,y
    return True

def move(x,y):# 목적지까지 이동 하기.
    global battery,cx,cy
    lx,ly = p[(x,y)]
    q = deque()
    q.append((x,y,0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,cnt = q.popleft()
        if x == lx and y == ly:
            if cnt > battery:# 도달은 가능하지만, 연료가 부족하면 False
                return False
            battery -= cnt
            battery += (cnt*2)# 도착시, 소모한 연료의 2배가 충전.
            cx,cy = lx,ly
            return True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] =1
                q.append((nx,ny,cnt+1))
    return False

while len(p)> 0:# 모두 다 태우고 이동했다면 종료. 한명이라도 태울 수 없는 경우 또는 중간에 연료가 소진 되면 종료
    target = choose()
    if target == False:
        print(-1)
        break

    tx,ty,dist = target
    if pickUp(tx,ty,dist) == False:
        print(-1)
        break

    if move(tx,ty) == False:
        print(-1)
        break
    del p[(tx,ty)]
else:
    print(battery)
