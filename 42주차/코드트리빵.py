from collections import deque
n, m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
target = {}# 목적지를 담은 딕셔너리.

for i in range(1,m+1):# m명의 목적지 할당.
    a,b = map(int,input().split())
    target[i] = [a-1,b-1]
dx = [-1,0,0,1]# 상 좌 우 하 순으로 이동.
dy = [0,-1,1,0]

people = {}# 사람들의 위치를 나타낼 배열.
cnt = m # 편의점에 도착하지 않은 사람들.
time = 1 # 현재 시간.
def move():# 격자에 있는 모든 사람이 최단거리로 편의점에 도착할 수 있는 방향으로 이동.
    global g,people,cnt
    new = {}
    for num in people:
        sx,sy = people[num]# 현재 위치
        tx,ty = target[num]# 목적지
        q = deque()
        q.append((0,sx,sy,[]))
        visited = [[0]*n for _ in range(n)]
    
        visited[sx][sy] = 1
        while q:
            dist,x,y,route = q.popleft()# 지금까지의 거리, 좌표, 이동하는 방향 route(배열)
            if x == tx and y == ty:# 도착지에 도달했을 때가 가장 최단거리인 경우이며, 다음에 이동할 좌표로 할당.
                nextX = sx+ dx[route[0]]
                nextY = sy+ dy[route[0]]
                people[num] = [nextX,nextY]
                break
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < n and 0<= ny < n and g[nx][ny] != -1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((dist+1,nx,ny,route+[i]))# 이동가능한 방향 쌓기. route+[i].
    for num in people:# 이동 이후에 편의점 도착 여부 확인.
        sx,sy = people[num]
        tx,ty = target[num]
        if sx == tx and sy == ty:# 편의점에 도착한다면! cnt-1, 이제 해당 좌표는 접근 불가.
            cnt -= 1
            g[sx][sy] = -1
        else:
            new[num] = [sx,sy] # 편의점 도착이 아니라면, 그대로
    people=new

def baseCamp(num): # num번 사람이 베이스 캠프로 이동. 편의점과 가장 가깝고 행과 열의 번호가 가장 작은 곳 선정
    global people,g
    tx,ty = target[num]
    q= deque()
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] =1
    q.append((0,tx,ty))
    cand = []
    while q:
        dist,x, y= q.popleft()
        if g[x][y] == 1:
            cand.append((dist,x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0<= ny < n and g[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((dist+1,nx,ny))
    cand.sort(key=lambda x:(x[0],x[1],x[2]))
    ex,ey = cand[0][1],cand[0][2]
    people[num] = [ex,ey] # 베이스 캠프로 이동.
    g[ex][ey] = -1# 이제 해당 좌표로 접근 불가.

while True:
    if len(people) > 0:# 격자에 사람이 있다면, 이동.
        move()
       
    if time <= m:# m초 이하라면, 베이스 캠프로 time번 사람이 이동함.
        baseCamp(time)
        
    if cnt == 0:# 모두가 편의점에 도착하면 break
        print(time)
        break
    time += 1
# 코드트리 빵 복습