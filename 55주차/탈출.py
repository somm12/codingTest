from collections import deque
r,c = map(int,input().split())
g = []
water = deque()
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*c for _ in range(r)]
for i in range(r):
    g.append(list(input()))
    for j in range(c):
        if g[i][j] == '*':
            water.append((i,j,0))
        elif g[i][j] == 'S':
            q.append((i,j,0))
            visited[i][j] = 1

def inRange(x,y):
    return 0 <= x < r and 0 <= y < c
def bfs():
    count = 0
    while q:# 물 먼저 이동. => 물이 찰 예정인 곳은 고슴도치가 이동 못하므로, 먼저 이동 시키기.
        while water and water[0][2] <= count:
            x,y,time = water.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if inRange(nx,ny):
                    if g[nx][ny] == 'S' or g[nx][ny] == '.':# 빈곳 또는 고슴도치가 있는곳 이동 가능.
                        g[nx][ny] = '*'
                        water.append((nx,ny,time+1)) 
        
        while q and q[0][2] <= count:# 고슴도치 이동.
            x,y,time = q.popleft()
            if g[x][y] == 'D':
                return time
            
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if inRange(nx,ny) and not visited[nx][ny]:
                    if g[nx][ny] != 'X' and g[nx][ny] != '*':# 돌, 물이 차있는곳은 이동 불가.
                        visited[nx][ny] = 1
                        q.append((nx,ny,time+1)) 
        
        count += 1
      
    return 'KAKTUS'
print(bfs())