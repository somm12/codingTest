from collections import deque
n, q = map(int,input().split())
ice = []
N = (2**n)
for _ in range(N):
    ice.append(list(map(int,input().split())))

arr = list(map(int,input().split()))

dx = [0,1,-1,0]# 우 하 상 좌 방향으로 이동.for 반복문 방문 순서대로 얼음이 움직이는 방향.
dy = [1,0,0,-1]
def inRange(x,y):
    return 0 <= x < N and 0 <= y < N

def rotate(L):
    global ice
    tmp = [[0]* N for _ in range(N)]
    for sx in range(0,N,2**L):
        for sy in range(0,N,2**L):
            idx = 0
            for mx in range(sx, sx+ (2**L), 2**(L-1)):
                for my in range(sy, sy+ (2**L), 2**(L-1)):
                    for x in range(2**(L-1)):
                        for y in range(2**(L-1)):
                            px,py = mx+x, my + y
                            nx,ny = px + dx[idx]*(2**(L-1)), py + dy[idx]*(2**(L-1))
                            tmp[nx][ny] = ice[px][py]
                    idx += 1
    ice = tmp
def melting():# 인접한 얼음이 3개 미만이면 녹음.
    global ice
    tmp = [[0]*N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if ice[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx,ny = x+dx[i], y +dy[i]
                    if inRange(nx,ny) and ice[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    tmp[x][y] = ice[x][y] -1
                else:
                    tmp[x][y] = ice[x][y]
    ice = tmp

def bfs(x,y):# 가장 큰 얼음 덩어리 찾기.
    visited[x][y] = 1
    q= deque()
    q.append((x,y))
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx,ny = dx[i]+x, y + dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and ice[nx][ny] > 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt

for L in arr:
    if L > 0:# L 이 0 이면 그대로.
        rotate(L)
    melting()
   
remain = 0
size = 0

for x in range(N):
    for y in range(N):
        remain += ice[x][y]

visited = [[0]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if not visited[x][y] and ice[x][y] > 0:
            cnt = bfs(x,y)
            size = max(size, cnt)

print(remain)
print(size)