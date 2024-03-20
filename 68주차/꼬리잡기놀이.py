from collections import deque

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

answer =0
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def inRange(x,y):
    return 0<=x<n and 0 <= y < n

def bfs(x,y,visited):
    q=deque()
    q.append((x,y))
    t = []
    while q:
        x,y = q.popleft()
        t.append((x,y))
        if g[x][y] == 3:
            break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and 1 <= g[nx][ny] <=3:
                if g[x][y] == 1:
                    if g[nx][ny] == 2:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                elif g[x][y] == 2:
                    if g[nx][ny] == 2 or g[nx][ny] == 3:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
    return t

def move(team):
    global g
    hx,hy = team[0]
    nT = []
    for i in range(4):
        nx,ny = hx+dx[i], hy+dy[i]
        if inRange(nx,ny) and (g[nx][ny] == 3 or g[nx][ny] == 4):
            nT.append((nx,ny))
            if g[nx][ny] == 4:
                tx,ty = team[-1]
                g[tx][ty] = 4
            break
    team.pop()
    nT = nT + team
    for i in range(len(nT)):
        x,y = nT[i]
        if i == 0:
            g[x][y] = 1
        elif i == len(nT) - 1:
            g[x][y] = 3
        else:
            g[x][y] = 2

def findThrow():


    r = (round)%(4*n)# 4n을 주기로 공 던지기 패턴이 다름. 공을 던지는 시작점과 방향을 반환.
    if r < n:
        return [r,0,0]
    elif n <= r < 2*n:
        return [n-1, r - n, 1]
    elif (2*n) <= r < 3*n:
        return [-r + (3*n-1), n-1, 2]
    return [0,(4*n)-1 -r , 3]

def throwBall(sx,sy,d):
    global answer, g
    nx,ny = sx,sy

    for _ in range(n):
        for t in teams:
            for i in range(len(t)):
                tx,ty = t[i]
                if nx == tx and ny == ty:
                    nth= i+1
                    answer += (nth**2)
                    fx,fy = t[0]
                    ex,ey = t[-1]
                    g[fx][fy] = 3
                    g[ex][ey] = 1
                    return
        nx += dx[d]
        ny += dy[d]

def findTeams():
    arr = []
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if g[x][y] == 1:
                visited[x][y]=1
                tmp = bfs(x,y,visited)
                if len(tmp) >= 3:
                    arr.append(tmp)
    return arr

for round in range(k):
    teams = findTeams()# 팀 찾기

    for team in teams:
        move(team)# 팀 이동
    teams = findTeams()# 이동 후 다시 팀찾기

    sx,sy,d = findThrow()# 공던지는 위치 찾기
    throwBall(sx,sy,d)# 공을 던져서, 점수획득, 머리 사람 꼬리 사람 바뀜

print(answer)
