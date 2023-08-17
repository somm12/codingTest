from collections import deque
n,m,fuel = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
tx,ty = map(int,input().split())

tx -=1# 택시 위치
ty -= 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
people = {}# 사람들 정보 담기.
for _ in range(m):
    a,b,c,d = map(int,input().split())
    people[(a-1,b-1)] = (c-1,d-1)

def choose():# 후보 정하기. bfs 탐색으로 승객과의 거리를 구한다.
    global people
    cand= []
    
    q = deque()
    q.append((tx,ty,0))
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] =1
    while q:
        x,y,dist = q.popleft()
        if (x,y) in people:# 이동 중에, 승객 좌표를 만나면, 그 때까지의 거리를 저장.
            cand.append((dist,x,y, people[(x,y)][0], people[(x,y)][1]))
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = 1# 방문 처리.
                q.append((nx,ny,dist+1))# 거리 +1
    if len(cand) != len(people):# 만약 현재 남은 승객을 모두 태울 수 없는 거라면 -1.
        return -1
    
    cand.sort()# 정렬해서 가장 가까운거리의 승객을 태운다.
    a,b = cand[0][1],cand[0][2]
    del people[(a,b)]# 한 분 태우면 사전에서 삭제. 승객의 모든 출발점이 다르므로 괜찮음.
    return cand[0]

def moveStart(target):# 승객이 있는 출발지로 이동.
    global fuel,tx,ty
    dist,sx,sy,ex,ey = target
    if fuel < dist:# 연료가 부족하면 False
        return False
    fuel -= dist # 연료 소모, 택시 이동
    tx,ty = sx,sy
    return True

def moveDesti(target):# 연료 소모한 만큼 2배를 충전, 택시를 목적지까지 이동.
    global fuel, tx,ty
    ex,ey = target[3],target[4]
    q = deque()
    q.append((tx,ty,0))
    visited =[[0]*n for _ in range(n)]
    visited[tx][ty] = 1

    while q:
        x,y,cost = q.popleft()
        if [x,y] == [ex,ey]:
            if fuel < cost:# 이동을 했지만 연료가 중간에 소모가 되는 경우 False
                return False
            tx,ty = ex,ey
            fuel -= cost
            fuel += (cost*2)
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] =1
                q.append((nx,ny,cost+1))
            
    return False# 목적지로 갈 수 없는 경우 False(벽으로 둘러쌓여 있는.)
while m > 0:# 모든 승객을 태울 수 있는지.
    target = choose()
    
    if target == -1:# 승객을 다 태우지 못하는 경우.
        print(-1)
        break
    if not moveStart(target):# 연료가 중간에 소모가 된다면 종료.
        print(-1)
        break
    if not moveDesti(target):# 연료 중간에 소모가 된다면 종료.
        print(-1)
        break

    m -= 1
else:# break없이 끝까지 모두를 태웠다면 남은 연료를 출력.
    print(fuel)

