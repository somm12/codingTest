from collections import deque
n,L,R = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dx =[-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

def inRange(x,y):
    return 0 <= x< n and 0 <= y < n

def bfs(x,y):
    global visited
    q= deque()
    q.append((x,y))
    visited[x][y] = 1
    team = []
    while q:
        x,y =q.popleft()
        team.append((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny]:
                if L <= abs(g[x][y]- g[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return team

def move():
    global g
    for arr in teams:
        total = 0
        size = len(arr)
        for x,y in arr:
            total += g[x][y]
        value = total//size
        for x,y in arr:
            g[x][y] = value
            
while True:
    visited = [[0]*n for _ in range(n)]
    teams =[]
    for x in range(n):# 결국 연합을 만드는 것 = bfs/dfs로 연결된 덩어리 만들기.
        for y in range(n):
            if not visited[x][y]:
                teams.append(bfs(x,y))
    
    if len(teams) == n*n:# 연합이 만들어지지 않았음.
        break
    move()# 인구 이동.
    answer += 1
    

print(answer)

# 백준 인구이동.