import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer= -1
n, m = map(int,input().split())

g = []
max_val = -1
for i in range(n):
    g.append(list(map(int,input().split())))
    max_val = max(max(g[i]),max_val)
visited = [[0]*m for _ in range(n)]

def dfs(x,y,total,cnt):
    global answer

    if answer >= total + (max_val*(4-cnt)):
        return
    if cnt == 4:
        answer = max(total,answer)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt ==2:
                visited[nx][ny] = 1
                dfs(x,y,total+g[nx][ny],cnt+1)
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, total + g[nx][ny], cnt + 1)
            visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,g[i][j],1)
        visited[i][j] = 0
print(answer)

# 테트로미노