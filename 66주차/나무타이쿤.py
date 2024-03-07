n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

info = [# 초기 영양제 위치.
    (n-2,0),(n-2,1), (n-1,0),(n-1,1)
]
mx = [0,-1,-1,-1,0,1,1,1]
my = [1,1,0,-1,-1,-1,0,1]

def inRange(x,y): # 격자 범위 내 인지 검사.
    return 0 <= x < n and 0 <= y < n

def move():# 영양제 이동. 행과 열 끝은 연결 됨.
    global info
    tmp = []
    for x,y in info:
        nx,ny = (x+(mx[d]*p))%n , (y + (my[d] * p)) % n
        tmp.append((nx,ny))
    info = tmp

def put():# 영양제 투입.
    global g
    for x,y in info:
        g[x][y] += 1

def grow():
    global g
    for x,y in info:
        for cx, cy in [(-1,-1),(-1,1), (1,-1),(1,1)]:# 대각선 방향으로 1이상인 개수 만큼 증가.
            nx,ny = x+cx, y+cy
            if inRange(nx,ny) and g[nx][ny] >= 1:
                g[x][y] += 1
def refresh():
    global info,g

    tmp = []
    infoSet = set(info)
    for x in range(n):
        for y in range(n):
            if (x,y) not in infoSet and g[x][y] >= 2:# 영양제가 투입된 땅 제외, 높이가 2이상은 나무 -2 & 영양제 올려두기.
                g[x][y] -=2
                tmp.append((x,y))
    info = tmp
    
for _ in range(m):
    d,p = map(int,input().split())
    d -= 1
    move()
  
    put()
    
    grow()
   
    refresh()
   

answer = 0
for x in range(n):
    for y in range(n):
        answer += g[x][y]
print(answer)