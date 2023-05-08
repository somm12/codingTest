from collections import deque
n,m = map(int,input().split())
answer = 0
g = []
e = []# 빈 칸 위치를 담을 배열
v = []# 바이러스 위치를 담을 배열
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if g[i][j] == 0:
            e.append((i,j))
        elif g[i][j] == 2:
            v.append((i,j))

def wall(L,start):# 백트래킹으로 벽 3개를 설치.(조합)
    global g
    if L == 3:
        virus() # 벽 3개 설치한 뒤, 바이러스 퍼뜨리기.
        return
    for i in range(start,len(e)):
        x,y = e[i][0], e[i][1]
        g[x][y] = 1
        wall(L+1,i+1)
        g[x][y] = 0

def virus():
    temp = [[0]*m for _ in range(n)] # 현재 연구소 2차원 배열 값을 복사해서 바이러스 퍼뜨림.
    for i in range(n):
        for j in range(m):
            temp[i][j] = g[i][j]
    q = deque() # 바이러스 위치를 담은 배열을 q에 복사
    for i in v:
        q.append(i)
    while q: # 상 하 좌 우 방향으로 바이러스가 퍼짐. BFS
        x,y = q.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and temp[nx][ny] == 0:# 빈칸으로만 퍼짐
                temp[nx][ny] = 2
                q.append((nx,ny))
    area(temp) # 바이러스가 다 퍼진 후, 면적을 구하는 area 함수 호출.

def area(arr):
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    answer = max(answer,cnt) # 안전영역 값 update

wall(0,0)
print(answer)