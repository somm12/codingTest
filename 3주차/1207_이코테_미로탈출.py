from collections import deque
n, m = map(int, input().split())
arr = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if arr[nx][ny] == 1 and not visited[nx][ny]:
            arr[nx][ny] = arr[x][y] + 1
            dfs(nx, ny)
dfs(0,0)
print(arr[n-1][m-1])

def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                arr[nx][ny] = arr[a][b] + 1
                q.append((nx, ny))
                visited[nx][ny] = True
bfs(0,0)
print(arr[n-1][m-1])

# dfs, bfs 둘 다 풀 수 있지만, dfs 200*200이 최대이므로 파이썬은 기본 1000으로 재귀 깊이 설정이 됨.
# 따라서 재귀의 제한을 따로 둬야하기 때문에 이를 고려하지 못했을 경우를 생각하면,
#  bfs를 쓰면 좀 더 실수를 덜할 것.