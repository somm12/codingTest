import copy
R,C,T = map(int,input().split())
AC = []
dust = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for i in range(R):
    graph.append(list(map(int,input().split())))
    for j in range(C):
        if graph[i][j] == -1:
            AC.append((i,j))

def diffusion():
    arr = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        arr[nx][ny] += graph[i][j]//5
                        tmp += graph[i][j]//5
                graph[i][j] -= tmp
    for i in range(R):
        for j in range(C):
            graph[i][j] += arr[i][j]

# 순환하기.
def clean_up():
    up_step = [[0,1],[-1,0],[0,-1],[1,0]]
    d = 0
    x,y = AC[0]
    # 시작 위치
    up, y = x,1
    previous = 0
    while True:
        nx, ny = x + up_step[d][0], y + up_step[d][1]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1
            continue
        previous, graph[x][y] = graph[x][y], previous
        x,y = nx,ny
    return

def clean_down():
    down_step = [[0,1],[1,0],[0,-1],[-1,0]]
    d = 0
    x,y = AC[1]
    # 시작 위치
    down, y = x,1
    previous = 0
    while True:
        nx, ny = x + down_step[d][0], y + down_step[d][1]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1
            continue
        previous, graph[x][y] = graph[x][y], previous
        x,y = nx,ny
    return
for _ in range(T):
    diffusion()
    clean_up()
    clean_down()

ans = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            ans += graph[i][j]
print(ans)
