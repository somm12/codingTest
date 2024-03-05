from collections import deque

n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y,visited):# g[x][y]와 색이 같고, 인접한 칸이면 같은 그룹 원소.
    visited[x][y] = 1
    value = g[x][y]
    q = deque()
    q.append((x,y))
    team = []
    while q:
        x,y = q.popleft()
        team.append((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == value:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return team

def findGroup():# 그룹 찾기.
    visited = [[0]*n for _ in range(n)]
    teams = []

    for x in range(n):
        for y in range(n):
            if not visited[x][y]:# 아직 방문안했다면 그룹 찾기 시작.
                teams.append(bfs(x,y,visited))
    return teams


def groupCombi():
    arr = []
    cnt = len(group)
    def dfs(start,res):
        if len(res) == 2:
            arr.append(res)
            return 
        for i in range(start, cnt):
            dfs(i+1, res+[i])
    dfs(0,[])
    return arr

def calcScore(a,b):# 그룹 a,b 간의 예술점수
    score = 0
    x1,y1= group[a][0]
    x2,y2 = group[b][0]
    score += (len(group[a]) + len(group[b]))
    score *= (g[x1][y1] * g[x2][y2])

    cnt = 0
    for x,y in group[a]:
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if inRange(nx,ny) and (nx,ny) in group[b]:# 맞닿은 변의 수 구하기.
                cnt += 1
    score *= cnt
    return score

def rotateBoard():
    global g

    tmp = [[0]*n for _ in range(n)]
    m = n//2

    for i in range(n):# 중앙 십자 부분 반시계방향 90 회전
        tmp[m][i] = g[i][m]
        tmp[i][m] = g[m][n-1-i]
    
    for sx,sy in [(0,0),(0,m+1),(m+1,0),(m+1,m+1)]:# 남은 4개 정사각형 시계방향 90회전
        for x in range(m):
            for y in range(m):
                tmp[sx + y][sy + m-1-x] = g[sx + x][sy + y]
    g = tmp

for nth in range(4):# 
    
    group = findGroup()# 모든 그룹 찾기

    arr = groupCombi()# 모든 그룹 쌍 조합.

    total = 0

    for a,b in arr:
        v = calcScore(a,b)# 그룹 쌍에 대한 예술 점수의 합.
        total += v
   
    answer += total
    if nth ==3:# 3회전 이후 예술점수를 합했다면 종료.
        break
    rotateBoard()# 회전
   
    

print(answer)