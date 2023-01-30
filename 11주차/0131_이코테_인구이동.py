from collections import deque

n,l, r = map(int, input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,idx):
    # 연합국가 담을 배열
    united = []
    united.append((x,y))
    q = deque([(x,y)])
    # 연합국가 번호 지정
    union[x][y] = idx
    united_sum = g[x][y]
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(g[x][y] - g[nx][ny]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = idx
                    cnt += 1
                    united_sum += g[nx][ny]
                    united.append((nx,ny))
    for i , j in united:
        g[i][j] = united_sum // cnt

total = 0
while True:
    union = [[-1] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i,j,idx)
                idx += 1
    if idx == n * n:
        break
    total += 1
print(total)