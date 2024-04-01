from collections import deque

n,q = map(int,input().split())
g = []
N = 2**n
dx = [0,1,-1,0]
dy = [1,0,0,-1]

for _ in range(N):
    g.append(list(map(int,input().split())))
arr = list(map(int,input().split()))

def inRange(x,y):
    return 0 <= x < N and 0 <= y < N

def rotate():
    global g
    tmp = [[0]*N for _ in range(N)]

    for x in range(0,N, 2**L):# 2**L x 2**L 선택.
        for y in range(0,N,2**L):
            d = 0
            for i in range(x, x + (2**L), 2**(L-1)):# 2**L-1 2**L-1 형태로 4등분.
                for j in range(y, y+ (2**L), 2**(L-1)):
                    for a in range(i, i+(2**(L-1))):# 각각 회전 시키기
                        for b in range(j, j + (2**(L-1))):
                            nx = a+ (dx[d] * (2**(L-1))) # 각 칸은 2**L-1 만큼씩 이동.
                            ny = b + (dy[d] * (2**(L-1)))
                            tmp[nx][ny] = g[a][b]

                    d = (d+1)%4
    g = tmp

def melting():
    global g
    tmp = [li[:] for li in g]
    for x in range(N):
        for y in range(N):
            if g[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if inRange(nx,ny) and g[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    tmp[x][y] -= 1
    g = tmp

def bfs(x,y,visited):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x +dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] > 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return cnt

for L in arr:

    if L > 0:# 0 레벨은 회전 후에 변화가 없음.
        rotate()
    melting()
 

answer = 0
for x in range(N):
    for y in range(N):
        answer += g[x][y]

print(answer)
if answer == 0:# 군집이 없는 경우.
    print(0)
else:
    size = 0
    visited = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and g[x][y] > 0:# 가장 큰 군집 크기 구하기
                size = max(size, bfs(x,y,visited))
    print(size)