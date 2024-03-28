dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]
g = []
n,m = map(int,input().split())
for _ in range(n):
    g.append(list(map(int,input().split())))

locat = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move(d,p):# 영양제 이동. 행과 열은 연결 됨.
    global locat
    tmp = []
    for x,y in locat:
        nx = (x + (dx[d] * p)) % n
        ny = (y + (dy[d] * p)) % n
        tmp.append((nx,ny))
    locat = tmp

def put():# 영양제 투입.
    global g
    for x,y in locat:
        g[x][y] += 1
def grow():# 투입한 땅의 나무 성장. 대각선에 1이상 높이 나무 개수 만큼. 단 격자 내 방향의 대각선만.
    global g
    for x,y in locat:
        for di in [1,3,5,7]:
            nx = x+dx[di]
            ny = y+dy[di]
            if inRange(nx,ny) and g[nx][ny] > 0:
                g[x][y] += 1

def cutTree():# 영양제 투입 땅 제외 칸 중. 2이상의 높이 나무 -2 베고, 영양제 올려둠.
    global locat, g
    s = set(locat)
   
    tmp = []
    for x in range(n):
        for y in range(n):
            if (x,y) not in s and g[x][y] >= 2:
                g[x][y] -= 2
                tmp.append((x,y))
    locat = tmp

for nth in range(1,m+1):
    d,p =map(int,input().split())
    d -= 1
    move(d,p)
    put()
    grow()
    cutTree()

answer = 0 # 남은 나무들의 높이 합.
for x in range(n):
    for y in range(n):
        answer += g[x][y]
print(answer)