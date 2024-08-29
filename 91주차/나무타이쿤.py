n,m = map(int,input().split())
arr = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
g = []
dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]
for _ in range(n):
    g.append(list(map(int,input().split())))

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move():
    global arr
    tmp = []
    for x,y in arr:
        nx = (x+ (dx[d]*p)) % n # 행과 열은 연결되어 있으므로, % n 필수.
        ny = (y+ (dy[d]*p)) % n
        tmp.append((nx,ny))
    arr = tmp

def put():
    global g
    for x,y in arr:
        g[x][y] += 1

def grow():
    global g
    for x,y in arr:
        cnt = 0
        for di in [1,3,5,7]:# 대각선 방향 1,3,5,7
            nx = x+dx[di]
            ny = y+dy[di]
            if inRange(nx,ny) and g[nx][ny] >= 1:
                cnt += 1
        g[x][y] += cnt

def buy():
    global g,arr
    s = set()
    tmp = []
    for x,y in arr:
        s.add((x,y))
    for x in range(n):
        for y in range(n):
            if (x,y) not in s and g[x][y] >= 2:
                g[x][y] -= 2
                tmp.append((x,y))
    arr = tmp

for _ in range(m):
    d,p = map(int,input().split())
    d -= 1# 방향 배열 인덱스 맞추기.
    move()# 방향, 칸수 대로 이동.

    put()# 영양제 투입 +1

    grow()# 인접 대각선 방향 1이상 높이 나무 수 만큼 나무 높이 성장

    buy()# 이전 영양제 제외한 부분들 중 2이상의 높이 나무로 영양제 구입.

answer = 0
for x in range(n):
    for y in range(n):
        answer += g[x][y]
print(answer)


# 코드트리 나무 타이쿤.