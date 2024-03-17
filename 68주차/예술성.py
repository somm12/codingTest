from collections import deque

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def bfs(x,y,visited):# 하나의 그룹 구하기.
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    color = g[x][y]
    team= []
    while q:
        x,y = q.popleft()
        team.append((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] =1
                q.append((nx,ny))
    return team

def groupCombination():# 그룹 끼리 번호쌍 조합.
    result = []
    length = len(group)
    def dfs(start,res):
        if len(res) == 2:
            result.append(res)
            return
        for i in range(start, length):
            dfs(i+1,res+[i])
    dfs(0,[])
    return result

def check(x,y,arr):# x,y가 arr에 속하는 위치인가 확인.
    for i,j in arr:
        if x==i and y == j:
            return True
    return False

def score(a,b):# 예술 점수 구하기
    g1 = group[a]
    g2 = group[b]
    v1 = g[g1[0][0]][g1[0][1]]
    v2 = g[g2[0][0]][g2[0][1]]
    point = 0
    point += (len(g1)+len(g2))
    point *= (v1*v2)
    
    cnt = 0
    for x,y in g1:
        for i in range(4):
            nx,ny = x+dx[i], y+ dy[i]
            if inRange(nx,ny) and check(nx,ny,g2):
                cnt += 1
    point *= cnt
    return point

def findGroup():# 그룹 찾기.
    teams = []
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                teams.append(bfs(x,y,visited))
    return teams

def rotate():
    global g
    tmp = [[0]*n for _ in range(n)]
    L = n//2
    for i in range(n):# 십자모양 회전. 
        tmp[L][i] = g[i][L]
        tmp[i][L] = g[L][n-1-i]        
    for sx,sy in [(0,0),(L+1,0),(0,L+1),(L+1,L+1)]:# 정사각형 회전
        for x in range(L):
            for y in range(L):
                tmp[sx + y][sy + L-1-x] = g[sx + x][sy+ y]
    g = tmp

for nth in range(4):
    group = findGroup()
    arr = groupCombination()
    total = 0
    for a,b in arr:
        total += score(a,b)
    answer += total
    if nth == 3:
        break
    rotate()
print(answer)