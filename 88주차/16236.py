from collections import deque
n = int(input())
g = []
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 9:
            sx,sy=i,j
            g[i][j] = 0
            
size= 2
time = 0
cnt = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def inRange(x,y):
    return 0 <= x< n and 0 <= y <n

def isNone():# 물고기 없는지?
    for x in range(n):
        for y in range(n):
            if 0 < g[x][y] < size:
                return False
    return True

def move():
    global time
    q = deque()
    q.append((sx,sy,0))
    visited = [[0]*n for _ in range(n)]
    visited[sx][sy] = 1
    cand = []
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] <= size:
                visited[nx][ny] = 1
                q.append((nx,ny,dist+1))
                if g[nx][ny] < size and 1 <= g[nx][ny] <= 6:
                    
                    cand.append((dist+1,nx,ny)) # 물고기 후보.

    cand.sort(key=lambda x:(x[0],x[1],x[2]))
   
    

    return cand

while True:
   
    cand = move()
    if len(cand) == 0: break
    dist, sx,sy = cand[0]
    time+= dist
    g[sx][sy] = 0
    cnt += 1
    if size == cnt:
        size += 1
        
        cnt = 0

print(time)