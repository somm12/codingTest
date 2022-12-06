from collections import deque
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            dfs(nx, ny)
dfs(0,0)
print(arr[n-1][m-1])

def bfs(x, y):
    q = deque([(x,y)])
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[a][b] + 1
                q.append((nx, ny))
                
bfs(0,0)
print(arr[n-1][m-1])

# dfs, bfs 둘 다 풀 수 있지만, dfs는 재귀라서 시간초과 발생 가능. 최소거리는 bfs로 풀자.
