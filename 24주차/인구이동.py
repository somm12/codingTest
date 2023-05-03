from collections import deque
n, L,R = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def open(x,y):
    global visited
    unit = [] # 하나의 연합을 담을 배열
    q = deque()
    q.append((x,y))
    unit.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(g[x][y] - g[nx][ny]) <= R:# 차이가 L이상 R이하라면
                    visited[nx][ny]= 1
                    unit.append((nx,ny))# 연합 배열에 추가.
                    q.append((nx,ny))# 이어서 연합을 구하기 위해 q에도 추가
    return unit

def move(units):
    for arr in units:
        length = len(arr)
        tmp = 0
        for x,y in arr:
            tmp += g[x][y]
        p = tmp//length
        for x,y in arr:
            g[x][y] = p
while True:
    uniteds = [] # 매 인구이동 시, 총 연합 국가들의 좌표를 담을 배열
    visited = [[0]*n for _ in range(n)] # 매 인구이동 때마다 방문 여부 정보를 담는 배열
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:# 아직 방문하지 않은 국가라면 open함수로 연합을 구한다.
                unit = open(i,j)
                uniteds.append(unit)
    if len(uniteds) == n*n: # 국경선이 하나도 열리지 않으면 연합 국가의 수는 n*n과 같다. 이때 종료.
        break

    move(uniteds) # move함수를 통해 인구이동으로 바뀐 인구 수를 업데이트.
    cnt += 1 # 인구이동 횟수 증가
print(cnt)