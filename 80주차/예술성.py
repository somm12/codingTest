from collections import deque
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x < n and 0 <=y < n

def bfs(x,y,visited):# 각 그룹 좌표 배열 반환.
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    num = g[x][y]
    ret = []
    while q:
        x,y = q.popleft()
        ret.append((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == num:
                q.append((nx,ny))
                visited[nx][ny]=1
    return ret

def score(a,b):# a,b 그룹의 예술 점수 구하기.
    total = len(a) + len(b)
    x1,y1 = a[0]
    x2,y2 = b[0]
    total *= (g[x1][y1]*g[x2][y2])
    cnt = 0
    s = set()
    for x,y in b:
        s.add((x,y))
    for x,y in a:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx,ny) in s:
                cnt += 1
    total *= cnt
    return total

def rotate():
    global g
    L = n//2
    tmp = [[0]*n for _ in range(n)]
    # 십자가 부분
    for x in range(n):
        tmp[n-1-L][x] = g[x][L]

    for y in range(n):
        tmp[n-1-y][L] = g[L][y]

    # 정사각형 부분
    for sx,sy in [(0,0),(L+1,0),(0,L+1),(L+1,L+1)]:# 각 정사각형 시작점.
        for x in range(L):
            for y in range(L):
                tmp[sx + y][sy + L - 1 -x] = g[sx + x][sy + y]
    g = tmp


def getScore():
    global answer
    visited = [[0]*n for _ in range(n)]
    group = []
    total =0
    # 그룹 만들기.
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                arr = bfs(x,y,visited)
                group.append(arr)

    # 각 그룹의 모든 쌍의 점수 구하기.
    size = len(group)
    for i in range(size):
        for j in range(i+1,size):
            v = score(group[i],group[j])

            total += v

    return total

answer = 0
answer += getScore()# 초기 예술점수.


for _ in range(3):
    rotate()
    answer += getScore()
print(answer)
