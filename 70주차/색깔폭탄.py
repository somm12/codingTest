from collections import deque
dx =[-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

answer =0
def inRange(x,y):
    return 0 <=x < n and 0<= y < n

def bfs(x,y):
    color = g[x][y]
    q= deque()
    q.append((x,y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    arr = []
    red = 0
    while q:
        x,y = q.popleft()
        arr.append((x,y))
        if g[x][y] == 0:
            red += 1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and (g[nx][ny] == color or g[nx][ny] == 0 ) and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
    arr.sort(key=lambda x :(-x[0],x[1]))
    for x,y in arr:
        if g[x][y] != 0:# 기준점은 빨간색이 아닌 것 중에서, 행이 크고, 열이 작은 폭탄.
            cx,cy = x,y
            break
    
    return [arr, cx,cy,red]

def findBiggest():
    cand = []
    for x in range(n):
        for y in range(n):
            if 1 <= g[x][y] <= m:
                arr,cx,cy,red = bfs(x,y)
                if len(arr) > 1:# 총 개수가 2이상이어야함.
                    cand.append((arr,cx,cy,red))
    if len(cand) == 0:
        return False
    cand.sort(key= lambda x:(-len(x[0]),x[3],-x[1],x[2]))# 크기가 젤 크고, 빨간 폭탄개수가 적으며, 기준점 행이 크고, 기준점 열이 작은 순서로 우선순위.
    
    return cand[0][0]

def removeBombs():
    global g
    for x,y in bombs:
        g[x][y] = -2
def gravity():
    global g

    for y in range(n):
        for _ in range(n):# 최대 n칸 움직일 수 있음.
            for x in range(n-2,-1,-1):
                if g[x][y] >= 0 and g[x+1][y] == -2:# 폭탄이 있고, 앞에 빈칸이라면 swap
                    g[x][y],g[x+1][y] = g[x+1][y],g[x][y]

def rotate():
    global g
    tmp = [[-2]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tmp[n-1-y][x] = g[x][y]
    g =tmp

while True:
    bombs = findBiggest()# 가장 큰 폭탄 찾기.
    
    if bombs == False:
        break
    
    answer += (len(bombs)**2)
    removeBombs()# 폭탄 삭제
   
    gravity()# 중력 작용
   
    rotate()# 반시계 90도 회전
    
    gravity()# 다시 중력.
   
  
print(answer)