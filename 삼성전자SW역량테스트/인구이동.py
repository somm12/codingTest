from collections import deque
N,L,R = map(int,input().split())

g = []
for _ in range(N):
    g.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
time = 0
visited = [[0]*N for _ in range(N)]

def move(visited,g,i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    united = []
    total = g[i][j]
    united.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0<= ny < N and not visited[nx][ny]:
                if L <= abs(g[x][y] - g[nx][ny]) <= R:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    united.append((nx,ny))
                    total += g[nx][ny]

    for x,y in united:
        g[x][y] = (total//len(united))
    if len(united) == 1:
        return 0



while True:
    not_move = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move(visited,g,i,j)
                not_move += 1

    if not_move == N*N:
        break
    time += 1
print(time)