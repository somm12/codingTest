from collections import deque
n,m,fuel= map(int,input().split())
g = []

for _ in range(n):
    g.append(list(map(int,input().split())))
cx,cy = map(int,input().split())

cx -= 1
cy -= 1
people = {}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(m):
    sx,sy,ex,ey = map(int,input().split())
    people[(sx-1,sy-1)] = [ex-1,ey-1]
flag = True
cnt = m

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def find():
    q = deque()
    q.append((cx,cy,0))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    cand = []
    while q:
        x,y,distance = q.popleft()
        if (x,y) in people:
            cand.append((x,y,distance))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,distance+1))
    if len(cand)> 0:
        cand.sort(key = lambda x :(x[2],x[0],x[1]))# 최단거리 > 행이 작고 > 열이 작은 우선 순위
        tx,ty,distance = cand[0]
        if distance > fuel:
            return -1# 이동 도중에 연료가 바닥나는 경우
        return cand[0]
    return - 1# 아예 승객을 태울 수 없는 경우
def move():
    ex,ey = people[(cx,cy)]
    q = deque()
    q.append((cx,cy,0))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    while q:
        x,y,distance = q.popleft()
        if x == ex and y == ey:
            if fuel < distance:# 연료가 이동 중에 바닥.
                return -1
            return distance
        for i in range(4):
            nx,ny = x+dx[i],y +dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,distance+1))
    return -1# 목적지 칸에 접근을 할 수 없다면.


while cnt > 0:# 승객을 모두 태울때까지.
    tmp = find()
    if tmp == -1:#승객을 태울 수 없거나, 연료가 바닥나면
        flag=False
        break
    tx,ty,dist = tmp
    fuel -= dist
    cx,cy = tx,ty
    dist = move()
    if dist == -1:#목적지 까지 접근할 수 없거나 연료가 부족한 경우
        flag= False
        break
    cx,cy = people[(tx,ty)]
    fuel -=dist
    fuel+= (dist*2)
    cnt -= 1
    del people[(tx,ty)]# 승객을 목적지까지 태우고 난 후, people에서 삭제.

if flag:
    print(fuel)
else:# 모두 태울 수 없음.
    print(-1)