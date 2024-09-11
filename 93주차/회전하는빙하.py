from collections import deque
n,q = map(int,input().split())
N = 2**n
g = []
for _ in range(N):
    g.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def inRange(x,y):
    return 0 <= x < N and 0 <= y < N

def rotate(L):
    global g
    tmp = [[0]*N for _ in range(N)]
    k = 2**L
    m = 2**(L-1)

    for sx in range(0,N,k):
        for sy in range(0,N,k):
            d = 0

            for x in range(sx,sx+ k,m):# 2**L-1 2**L-1 격자 선택.
                for y in range(sy,sy+k,m):

                    for i in range(x,x+m):# 해당 격자에서의 좌표들. 모두 d라는 방향으로, m만큼씩 이동한다.
                        for j in range(y,y+m):
                            nx,ny = i+(dx[d]*m),j+(dy[d]*m) 
                            tmp[nx][ny] = g[i][j]
                    d += 1
    g = tmp

def melting():
    global g
    tmp = [v[:] for v in g]
    for x in range(N):
        for y in range(N):
            if g[x][y] == 0:
                continue
            cnt = 0
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if inRange(nx,ny) and g[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:# 인접한 칸에 개수가 3개이상이 아니면 -1 녹는다.
                tmp[x][y] -= 1
    g= tmp

def bfs(x,y,visited):# x,y 좌표 주변의 군집 넓이 구하기.
    q= deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt

def bigArea():# 가장 큰 군집 넓이 구하기.
    maxV = 0
    visited = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if g[x][y] > 0 and not visited[x][y]:
                maxV = max(maxV, bfs(x,y,visited))
    return maxV

for L in arr:
    if L != 0:
        rotate(L)
    melting()



big = bigArea()
answer =0
for x in range(N):
    for y in range(N):
        answer += g[x][y]
print(answer)
print(big)

# 코드트리 문제