from collections import deque
n,m,fuel = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
tx,ty = map(int,input().split())
tx -= 1
ty -= 1
people = {}
flag = True
for _ in range(m):
    x,y,a,b = map(int,input().split())
    people[(x-1,y-1)] = (a-1,b-1)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def choose():# 가장 최단 거리의 승객 고르기.
    q = deque()
    q.append((tx,ty,0))
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1
    cand = []
    while q:
        x,y,dist = q.popleft()
        if (x,y) in people:
            cand.append((dist,x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 0:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = 1
    if len(people) != len(cand):# 만약 모두 태울 수 없는 경우라면 False
        return False
    cand.sort(key=lambda x:(x[0],x[1],x[2]))# 거리 > 행 > 열 이 작은 순으로 정렬.
    return cand[0]
        
def pickUp(x,y,dist):# 선택한 승객 위치로 이동.
    global fuel, tx,ty

    if fuel >= dist:# 남은 연료가 충분하다면 True.
        fuel -= dist
        tx,ty = x,y
        return True
    return False
def go(a,b):# a,b 위치인 목적지로 향하는 함수.
    global tx,ty,fuel
    q = deque()
    q.append((tx,ty,0))
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1

    while q:
        x,y,dist = q.popleft()
        if x == a and y == b:# 목적지에 도착.
            if fuel >= dist:# 연료가 충분하다면, 거리의 2배만큼 연료충전, 거리만큼 연료 소모
                fuel -= dist
                fuel += (dist*2)
                tx,ty = a,b
                return True
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 0:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = 1
    return False

for _ in range(m):
    possible = choose()# 가장 거리가 짧고 행과 열의 번호가 작은 승객 찾기.
    if not possible: # 하지만 모든 승객을 태울 수가 없는 경우라면
        flag = False
        break
    dist,px,py = possible
    if pickUp(px,py,dist):# 승객 데리러 가기
        a,b = people[(px,py)]
        if go(a,b):# 목적지로 이동.
            del people[(px,py)]
            continue
        else:
            flag = False
            break
    else:
        flag = False
        break
else:
    print(fuel)

if not flag:# 승객을 태우지 못하는 경우나 연료가 중간에 소모된다면 -1
    print(-1)
