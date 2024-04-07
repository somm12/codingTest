from collections import deque

n,m,fuel = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
cx,cy= map(int,input().split())

cx -=1
cy -= 1
people = {}
for _ in range(m):
    sx,sy,ex,ey= map(int,input().split())
    people[(sx-1,sy-1)] = [ex-1,ey-1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <=x < n and 0 <= y < n

def choose():# 가장 가까운 승객 선택. 만약 모든 승객을 태울 수 없다면 False반환. 아니면 승객 위치와 거리 반환.
    q = deque()
    q.append((0,cx,cy))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    cand = []
    while q:
        dist,x,y = q.popleft()
        if (x,y) in people:
            cand.append((dist,x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((dist+1,nx,ny))
    if len(cand) == len(people):
        cand.sort(key = lambda x:(x[0],x[1],x[2]))
        need,x,y = cand[0]
        return [x,y,need]

    return False

def move(ex,ey):# 목적지 까지 도달하면 걸리는 거리 반환
    q = deque()
    q.append((cx,cy,0))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    while q:
        x,y,dist = q.popleft()
        if x == ex and y == ey:
            return dist
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,dist+1))
    return False

possible = True
while len(people) > 0:
    reach = choose()#승객 선택.
    if reach == False:# 승객을 태울 수없는 상황.
        possible = False
        break
    else:
        tx,ty,need = reach
        if need > fuel:# 연료 부족.
            possible = False
            break
        else:
            cx,cy = tx,ty
            fuel -= need
    ex,ey = people[(tx,ty)]# 승객의 목적지.
    need = move(ex,ey)
  
    if need == False or need > fuel:# 승객이 목적지 까지 못가는 상황 이거나 연료가 부족한 경우.
        possible = False
        break
    else:
        fuel -= need
        fuel += (need*2)# 도착시, 소모된 연료 2배가 충전.
        cx,cy = ex,ey
        del people[(tx,ty)]# 도착한 승객은 제거.

if possible:
    print(fuel)
else:# 모두 태울 수 없다면 -1.
    print(-1)
