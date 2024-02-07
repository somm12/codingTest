n,m = map(int,input().split())
g = []
pills = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]# 초기 영양제 위치.
dx = [0,-1,-1,-1,0,1,1,1]# 영양제 이동 방향
dy = [1,1,0,-1,-1,-1,0,1]
cx = [-1,-1,1,1]# 인접 4방향 대각선
cy = [-1,1,1,-1]

for _ in range(n):
    g.append(list(map(int,input().split())))
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def move():# 영양제 이동. 행과 열 연결
    global pills
    tmp  =[]
    for x,y in pills:
        nx = (x + (dx[d] * p)) % n
        ny = (y + (dy[d] * p)) % n
        tmp.append((nx,ny))
    pills = tmp
def put():# 영양제 투입
    global g
    for x,y in pills:
        g[x][y] += 1
def grow():# 영양제 투입 후, 성장
    global g
    for x,y in pills:
        cnt = 0
        for i in range(4):
            nx,ny = x+cx[i],y+cy[i]
            if inRange(nx,ny) and g[nx][ny] >=1:
                cnt += 1
        g[x][y] += cnt

def buyPill():# 영양제 새로 사기, 투입된 위치 제외 높이가 2이상인 부분 -2
    global pills
    tmp = []
    s = set(pills)
    for x in range(n):
        for y in range(n):
            if g[x][y] >= 2 and (x,y) not in s:
                g[x][y] -= 2
                tmp.append((x,y))
    pills = tmp

for _ in range(m):
    d,p = map(int,input().split())
    d -= 1
    move()

    put()
   
    grow()
  
    buyPill()
  

answer = 0
for x in range(n):
    for y in range(n):
        answer += g[x][y]
print(answer)