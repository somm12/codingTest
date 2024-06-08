import sys
input = sys.stdin.readline
n,m =map(int,input().split())
g = []
maxV = 0
for i in range(n):
    g.append(list(map(int,input().split())))
    maxV =max(maxV, max(g[i]))
visited = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

def inRange(x,y):
    return 0 <= x< n and 0 <= y < m

def dfs(L,x,y,total):
    global answer
    if L == 4:
        answer = max(answer, total)
        return
    if total + ((4-L)*maxV) <= answer:# 이미 최대값으로 모두 더해진다해도 지금까지의 합의 최대인 answer이하라면 그만 재귀하기.
        return
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if inRange(nx,ny) and not visited[nx][ny]:
            if L !=2:
                visited[nx][ny] = 1
                dfs(L+1,nx,ny,total+g[nx][ny])
                visited[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                dfs(L+1,x,y,total+g[nx][ny])
                dfs(L+1,nx,ny,total+g[nx][ny])
                visited[nx][ny] = 0
        
for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        dfs(1,x,y,g[x][y])
        visited[x][y] = 0
print(answer)
#백준 테르노미노