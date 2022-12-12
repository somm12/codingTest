import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int (input())


def dfs(x, y, graph):
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >=m:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny,graph)


for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j, graph)
                cnt += 1
    print(cnt)