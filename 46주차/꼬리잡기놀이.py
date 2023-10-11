n,m,k= map(int,input().split())
g = []

for _ in range(n):
    g.append(list(map(int,input().split())))
answer =0
dx =[-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,visited):
    visited[x][y] =1
    res = [(x,y)]
    def d(sx,sy):
        for i in range(4):
            nx = sx+dx[i]
            ny = sy+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if g[sx][sy] == 1:# 1일 때는 2 찾기.
                    if g[nx][ny] == 2:
                        visited[nx][ny] = 1
                        res.append((nx,ny))
                        d(nx,ny)
                else:# 2일 때는 2 또는 3 찾기.
                    if 1< g[nx][ny] <4:
                        visited[nx][ny] = 1
                        res.append((nx,ny))
                        d(nx,ny)
    d(x,y)
    return res
def findTeam():# 팀을 찾는 함수.
    global team
    visited = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if g[x][y] == 1:
                arr = dfs(x,y,visited)
                team.append(arr)

def move():# 한칸씩 움직임
    global team, g
    newTeam = []
    for t in team:
        arr = []# 한팀의 이동 후의 좌표들을 담을 배열 .
        hx,hy = t[0]
        for i in range(4):
            nx = hx+dx[i]
            ny = hy+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == 4:# 머리와 꼬리가 붙은 경우가 아닐때
                    arr.append((nx,ny))
                    arr += t[:]
                    ptx,pty = arr.pop() # 이전 팀의 꼬리 부분이였던 좌표 반환
                    g[ptx][pty] = 4
                    break
                elif g[nx][ny] == 3:# 머리와 꼬리 붙은 경우 일때
                    arr.append((nx,ny))
                    arr += t[:]
                    arr.pop()
                    break
        newTeam.append(arr)
        for i,v in enumerate(arr):
            x,y = v
            if i == 0:
                g[x][y] = 1
            elif i == len(arr)-1:
                g[x][y] = 3
            else:
                g[x][y] = 2
    team = newTeam
def throwBall():# 공을 던지고 최초로 부딪히게 되는 좌표반환, 없다면 -1,-1 반환.
    now = (nRound)% (4*n)
    if 1 <= now <= n:
        for j in range(n):
            if 1 <= g[now -1][j] <= 3:
                return [now-1,j]
    elif n < now <= 2*n:
        for i in range(n-1,-1,-1):
            if 1 <= g[i][now - (n+1)] <= 3:
                return [i, now - (n+1)]
    elif 2*n < now <= 3*n:
        r = (now - (3*n))*-1
        for j in range(n-1,-1,-1):
            if 1 <= g[r][j] <= 3:
                return [r,j]
    else:
        c = (now - (4*n))*-1
        if now == 0:# 딱 4*n번째가 되어 now가 만약 0 이 라면,c가 음수가 되버림.
            for i in range(n):
                if 1<= g[i][0] <=3 :
                    return [i,0]
        else:
            for i in range(n):
                if 1<= g[i][c] <=3 :
                    return [i,c]
    return [-1,-1]

def point(tx,ty):# 점수를 획득하고, 머리와 꼬리가 바뀐다.
    global answer,g
    for t in team:
        for i,v in enumerate(t):
            x,y =v
            if [x,y]== [tx,ty]:
                answer += ((i+1)**2)
                hx,hy = t[0]# 머리
                lx,ly = t[-1]# 꼬리
                g[hx][hy] = 3
                g[lx][ly] = 1
                return

for nRound in range(1,k+1):
    team =[]
    findTeam()
    move()
    tx,ty = throwBall()
    if [tx,ty] != [-1,1]:
        point(tx,ty)

print(answer)