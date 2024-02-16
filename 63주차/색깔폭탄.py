from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n



def remove():# 폭탄 묶음 모두 제거하기.
    global g, answer
    for x,y in group:
        g[x][y] = -2
    C = len(group)
    answer += (C*C)

def gravity():
    global g
    for y in range(n):
        for _ in range(n):# 가장 맨위의 값이 맨 밑에까지 내려올 수 있기 때문에 n번 반복.
            for x in range(n-2,-1,-1):
                if g[x][y] >= 0 and g[x+1][y] == -2:
                    g[x][y],g[x+1][y] = g[x+1][y] , g[x][y]

def rotate():
    global g
    tmp = [[-2]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tmp[n-1-y][x] = g[x][y]
    g = tmp

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    color = g[x][y]
    team = []
    cnt = 0
    visited[x][y] = 1
    xy = []
    while q:
        x,y = q.popleft()
        team.append((x,y))
        if g[x][y] != 0:
            xy.append((x,y))
        else:
            cnt += 1
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and (g[nx][ny] == color or g[nx][ny] == 0):
                visited[nx][ny] = 1
        
                q.append((nx,ny))
    xy.sort(key = lambda x:(-x[0],x[1]))
    mx,my= xy[0]
    for i,j in team:
        if g[i][j] == 0:
            visited[i][j] = 0# 빨간 폭탄은 다른 폭탄과도 묶음이 될 수 있으므로, 방문처리 취소.
    return [team,cnt,mx,my]

def biggest():
    cand = []
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if g[x][y] > 0 and not visited[x][y]:
                team,cnt,x,y = bfs(x,y,visited)# 폭탄묶음 찾기. 빨간 폭탄 개수, 기준점 구하기.

                if len(team) > 1:# 폭탄이 2개이상이어야함.
                    cand.append([len(team),cnt,x,y] + team)
    if len(cand) > 0:
        cand.sort(key= lambda x : (-x[0],x[1],-x[2],x[3]))
        return cand[0][4:]
    return False# 폭탄 묶음이 없음.

while True:
    group = biggest()# 가장 큰 그룹 찾기.
    
    if group == False:
        break
    remove()# 삭제
    
    gravity()# 중력 작용
    
    rotate()# 반시계 회전
   
    gravity()
  
print(answer)