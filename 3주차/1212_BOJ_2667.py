import sys
input = sys.stdin.readline
n = int(input())
graph = []
ans = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        else:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for i in ans:
    print(i)