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
print(arr)

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
                
# bfs(0,0)
# print(arr)

# dfs, bfs 둘 다 풀 수 있지만, dfs는 깊이 우선 탐색이기 때문에, dx, dy 방향을 설정한 것에 우선순위를 둬서 탐색을 하게되어
# 최소거리를 구하지 못할 수 있으므로 최소거리 문제는 가까운 노드 부터 탐색하는 bfs로 풀자.
