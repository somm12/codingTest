import sys
sys.setrecursionlimit(10*1000)# 파이썬은 기본 재귀 제한이 1000. 이 문제는 2500번까지 가능.
dx = [-1,1,0,0]
dy = [0, 0,-1,1]
def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == 1:
            dfs(nx,ny)

T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    g = [[0]*m for _ in range(n)]
    for _ in range(k):
        y,x = map(int,input().split())
        g[x][y] = 1
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and g[x][y] == 1:
                dfs(x,y)
                cnt += 1# 덩어리 개수 세기
    print(cnt)
# 백준 유기농배추.
