import sys
sys.setrecursionlimit(10 ** 6)
n,m = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(input()))
dx= [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]

def inRange(x,y):
    return 0<= x < n and 0 <= y < m

def go(x,y):
    if not inRange(x,y) or g[x][y] == 'H':# 범위를 벗어나거나 구멍이면 거기까지만 이동이므로, 0을 반환.
        return 0 
    if visited[x][y]:# 이미 방문해서 사이클이 생김 -1 출력.
        print(-1)
        exit(0)
        
    if dp[x][y]:# 이미 값이 있으면 반환.
        return dp[x][y]

    visited[x][y] = 1
    value = int(g[x][y])
    
    for i in range(4):
        nx,ny = x + (value * dx[i]), y + (value * dy[i])
        dp[x][y] = max(dp[x][y], go(nx,ny) + 1)# 호출해서 +1 씩 더해서 재귀를 이용해 최대값을 구한다.
    
    visited[x][y] = 0
    
    return dp[x][y]

print(go(0,0))
# 백준 게임 - dp문제