from collections import deque

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dx = [1,0,-1,0]# 각 라운드 마다 공을 던질 때, 시작하는 좌표가 움직이는 방향. 하 우 상 좌
dy = [0,1,0,-1]

bx = [0,-1,0,1]# 공이 바라보는 방향. 우 상 좌 하
by = [1,0,-1,0]

answer =0
pattern = []

def inRange(x,y):
    return 0 <= x < n and 0<= y < n
def makePattern():# 공을 던지는 흐름 패턴 만들기. 시작 좌표, 던지는 방향.
    global pattern
    x,y = 0,0
    for d in range(4):
        for _ in range(n):
            pattern.append((x,y,d))
            x += dx[d]
            y += dy[d]
        x -= dx[d]
        y -= dy[d]
def bfs(x,y):# x,y를 시작점으로 하는 팀 찾기.
    q = deque()
    q.append((x,y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    team = []
    while q:
        x,y = q.popleft()
        team.append((x,y))
        if g[x][y] == 1:
            for i in range(4):
                nx,ny= x+dx[i],y+dy[i]
                if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == 2:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        elif g[x][y] == 2:
            for i in range(4):
                nx,ny= x+dx[i],y+dy[i]
                if inRange(nx,ny) and not visited[nx][ny] and (g[nx][ny] == 2 or g[nx][ny] == 3):
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    return team

def move():# 팀 이동. (머리가 이동할 좌표 + 기존 팀 좌표들(마지막 부분 제외))=> 팀 이동 후 모습.
    global g, teams

    newTeams =[]
    for team in teams:
        nt = []
        x,y = team[0]# 머리는 4 또는 3인 부분으로 이동.
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and (g[nx][ny] == 3 or g[nx][ny] == 4):
                nt.append((nx,ny))
                break
        tx,ty = team.pop()# 이전 꼬리는 제외.
        g[tx][ty] = 4# 격자 4로 채우기. 머리와 꼬리 붙은 경우, 떨어진 경우 모두.

        # 이동 후 격자에 머리사람 중간, 꼬리 사람 반영.
        for i in range(len(team)):
            x,y = team[i]
            nt.append((x,y))
            if i == len(team) - 1:# 마지막 부분은 꼬리.
                g[x][y] = 3
            else:
                g[x][y] = 2
        hx,hy = nt[0]
        g[hx][hy] = 1# 머리도 위치 넣기.
        newTeams.append(nt)
    teams = newTeams

def throw():# 공던지기.
    idx = round % (4*n)
    sx,sy,d = pattern[idx]
    while 0 <= sx < n and 0 <= sy < n:
        if g[sx][sy] in [1,2,3]:
            return [sx,sy]
        sx += bx[d]
        sy += by[d]
    return -1 # 아무도 충돌하지 않음

def getPoint(tx,ty):# 부딪히는 지점
    global answer
    for team in teams:
        cnt = 1
        for x,y in team:
            if x == tx and y == ty:
                answer += (cnt*cnt)
                return team
            cnt += 1

def headTailSwap():# 머리 꼬리 바뀜.
    global g
    hx,hy = targetTeam[0]# 머리 좌표
    tx,ty = targetTeam[-1]# 꼬리 좌표
    g[hx][hy] = 3
    g[tx][ty] = 1
            
def findTeam():
    allTeams = []
    for x in range(n):
        for y in range(n):
            if g[x][y] == 1:
                t = bfs(x,y)
                allTeams.append(t)
    return allTeams

makePattern()

for round in range(k):
    teams = findTeam()
    move()
    
    result = throw()
    if result != -1:
        rx,ry = result
        targetTeam = getPoint(rx,ry)
        headTailSwap()

print(answer)

