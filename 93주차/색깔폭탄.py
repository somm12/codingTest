from collections import deque

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x< n and 0 <= y < n

def bfs(x,y,visited):# 빨간색은 어디 묶음에도 속할 수 있으므로 방문처리를 하지 않는 것!!!!! 단 하나의 팀에서는 반복되지 않도록 set사용
    visited[x][y]= 1
    q = deque()
    q.append((x,y))
    arr = set()
    color = g[x][y]
    while q:
        x,y = q.popleft()
        arr.add((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny]:
                if g[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif g[nx][ny] == 0 and (nx,ny) not in arr:
                    q.append((nx,ny))

    return list(arr)

def findBig():
    cand  =[]
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and g[x][y] >= 1:
                arr = bfs(x,y,visited)
                if len(arr) < 2: continue# 2개이상은 되어야 묶음 .
                redCnt =0
                tmp =[]
                for i,j in arr:
                    if g[i][j] == 0:
                        redCnt += 1
                    else:
                        tmp.append((i,j))
                tmp.sort(key=lambda x: (-x[0],x[1]))# 기준점 찾기
                cx,cy = tmp[0]
                cand.append([len(arr),redCnt,cx,cy,arr])
    if len(cand) == 0:
        return False
    cand.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))# 크기가 크고, 빨간색개수가 적고, 기준점 행크고 열이 작은 순서 정렬.

    return cand[0][4]

def remove(ret):
    global g
    for x,y in ret:
        g[x][y] =-2# 빈 것 표시.
def gravity():
    global g
    tmp = [[-2]*n for _ in range(n)]
    for y in range(n):
        pos = n-1
        for x in range(n-1,-1,-1):
            if g[x][y] == -2: continue# 빈칸은 넘어감
            elif g[x][y] == -1:# 돌이라면, 표시해주고, 중력을 해도 돌은 그대로이므로 그 위의 행부터 착지 가능.
                tmp[x][y] = -1
                pos = x-1
                continue
            tmp[pos][y]= g[x][y]
            pos -= 1
    g = tmp

def rotate():
    global g
    tmp = [[-2]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tmp[n-1-y][x] = g[x][y]

    g = tmp

answer = 0
while True:
    ret = findBig()# 제일 큰 묶음.

    if ret == False:
        break
    C= len(ret)
    answer += (C*C)# 점수 획득.
    remove(ret)# 삭제
    gravity()# 중력
    rotate()# 반시계 회전

    gravity()

print(answer)
# 코드트리 문제