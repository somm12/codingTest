from collections import deque
answer = 0
n,m,k = map(int,input().split())

g = []
teams = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def findTeam(x,y,visited):
    team = []
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y,= q.popleft()
        team.append((x,y))
        if g[x][y] == 3:
            return team
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if g[x][y] == 1:
                    if g[nx][ny] == 2:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                else:
                    if g[nx][ny] in [2,3]:
                        q.append((nx,ny))
                        visited[nx][ny] = 1

def findAll():
    global teams
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                t= findTeam(i,j,visited)
                teams.append(t)
def move():# 모든 팀이 한 칸씩 이동
    global g, teams
    newTeams = []
    for team in teams:
        tmp = []
        for i in range(len(team)):
            x,y = team[i] # 현재 팀원 한 명의 좌표
            if i == 0:# 머리 일때는, 3또는 4와 만나는 부분이 다음에 이동할 좌표이다.
                for i in range(4):
                    nx,ny = x+dx[i], y+dy[i]
                    if 0 <= nx < n and 0 <= ny < n and g[nx][ny] in [3,4]:
                        tmp.append((nx,ny))
                        prev= (x,y)
                        break
            else:
                tmp.append(prev)
                prev= (x,y) # 그 이후의 좌표들이 이전 좌표에 도달할 수 있도록.
                flag = False
                for j in range(4):
                    nx = x+dx[j]
                    ny = y +dy[j]
                    if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 4:
                        flag = True # 만약 꼬리인 3 뒤가 4라면, 3 위치인 곳에 4 넣어야함.
                if i == len(team) -1:
                    if flag:
                        g[x][y] = 4 # 꼬리 부분은 4로 넣어야함.
                    
        newTeams.append(tmp)
    
    for team in newTeams:
        for i in range(len(team)):
            x,y = team[i]
            if i == 0:
                g[x][y] = 1
            elif 1<= i < len(team) - 1:
                g[x][y] = 2
            elif i == len(team) -1:
                g[x][y] = 3
    teams = newTeams

def location():# 정해진 선의 출발 점과, 방향을 return
    global round
    
    if 0 <= round < n:
        return [round, 0,3]# 우측으로
    if n <= round < 2*n:
        return [n-1, round-n, 0]# 위쪽으로

    if 2*n <= round < 3*n:
        return [ (round+ (-3*n + 1))*-1, n-1, 2]# 왼쪽으로

    if 3*n <= round < 4*n:
        return [0, (round+ (-4*n + 1))*-1, 1]# 아래쪽으로

def throwBall(x,y,d):# x,y 좌표에서 d방향으로 공을 던졌을 때, 마주치는 좌표 반환
    nx,ny=x,y
    while True:
        if g[nx][ny] in [1,2,3]:
            return [nx,ny]
        nx += dx[d]
        ny += dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            continue
        else:
            break
    return [-1,-1]

def changeHeadTail(teamIdx):# 머리와 꼬리 바꾸기.
    global teams,g
    
    teams[teamIdx][0],teams[teamIdx][-1] = teams[teamIdx][-1],teams[teamIdx][0]
    
    tmp = teams[teamIdx][1:-1]# 몸통 부분.
    # 머리와 꼬리가 바뀌면서 각 좌표의 순서도 반대가 되므로 적용하기.
    teams[teamIdx] = [teams[teamIdx][0]] + tmp[::-1] + [teams[teamIdx][-1]]


    hx,hy = teams[teamIdx][0]
    tx,ty = teams[teamIdx][-1]
    g[hx][hy] = 1 # g내에서도 숫자 머리 꼬리 바꾸기.
    g[tx][ty] = 3

def getScore(x,y):# x,y 좌표에서 공과 부딪혔을 때, 점수 획득 후, 해당 팀의 인덱스 반환.
    global answer
    for index, t in enumerate(teams):
        for idx,v in enumerate(t):
            i,j = v
            if i == x and j == y:
                answer += ((idx+1)**2) # 팀에서 k번째면 k제곱 만큼 더해짐.
                return index # 점수 획득한 팀의 인덱스 반환.

findAll()# 모든 팀 찾기

for round in range(k):
    round %= (4*n)

    move() # 한칸씩 이동.

    r,c,d =location()# 현재 라운드에 해당하는 공 던지는 정해진 선 구하기(r,c부터 시작해서 d방향을 가진 선)
    r,c = throwBall(r,c,d)# 던져서, 부딪히는 좌표 반환
    if [r,c] != [-1,-1]:# 빈 곳이 아니라면
        teamIdx = getScore(r,c)# 점수 획득, 해당 팀 인덱스 반환
        changeHeadTail(teamIdx)# 해당 팀 머리 꼬리 바꾸기.
    

print(answer)

# 놓친것1 : round 계산 => 1부터 시작하는 거라면, %= 연산을 했을 때, 다시 0이 되는 것에 조심해야함.
# 놓친것2 : 머리와 꼬리 이어진 경우. 바꿀 때, 먼저 모두 4을 할당하고, 이동될 좌표를 가지고 1,2,3 할당도 가능.
# 유의점 : 머리,꼬리 바꿀 때 중간 몸통 부분 방향도 바꿔야하는 것.