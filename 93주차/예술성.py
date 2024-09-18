from collections import deque

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <=x < n and 0 <= y < n

def calc(A,B):
    cnt = 0
    s = set(B)
    # 상하좌우 인접칸이 B에 해당하는 칸이면 인접하는 변이 1개씩 증가.
    for x,y in A:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (nx,ny) in s:
                cnt += 1
    return cnt


def bfs(x,y,visited):# 인접한 곳에 같은 색깔이면 한 그룹.
    visited[x][y] = 1
    tmp = []
    q= deque()
    q.append((x,y))
    color = g[x][y]
    while q:
        x,y = q.popleft()
        tmp.append((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == color:
                visited[nx][ny] = 1
                q.append((nx,ny))
    return tmp

def makeGroup():
    visited = [[0]*n for _ in range(n)]
    teams = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                t = bfs(x,y,visited)
                teams.append(t)
    return teams

def getScore():
    total = 0
    group = makeGroup()# 모든 그룹 만들기.
    L = len(group)
    # 그룹쌍만들기.
    for a in range(L):
        for b in range(a+1,L):
            A = group[a]
            B= group[b]
            x1,y1 = A[0]
            x2,y2 = B[0]
            # 칸수 더하고, 이루는 숫자 각 곱하기
            tmp = (len(A) + len(B)) * (g[x1][y1] * g[x2][y2])
            # 맞닿은 변수 수 구해서 곱하기.
            tmp *= calc(A,B)
            total += tmp
    return total


def rotate():
    global g

    tmp = [[0]*n for _ in range(n)]
    m = n//2
    # 십자가 모양 반시계 회전.
    for x in range(n):
        tmp[n-1-m][x] = g[x][m]
    for y in range(n):
        tmp[n-1-y][m] = g[m][y]
    # 나머지 정사각형 4개 각각 시계방향 회전.
    for sx,sy in [(0,0),(0,m+1),(m+1,0),(m+1,m+1)]:
        for x in range(m):
            for y in range(m):
                tmp[sx + y][sy + m-1-x] = g[sx + x][sy + y]

    g= tmp


answer = 0
for nth in range(4):
    score = getScore()# 점수 만들기
    answer += score

    if nth == 3: break # 3회전 이후 점수까지 계산 완료가 되었음.
    rotate()# 회전.

print(answer)
# 코드트리 예술성.