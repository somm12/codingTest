import sys
input = sys.stdin.readline
n,m = map(int,input().split())
g = []
answer = 0
maxV = -1
for i in range(n):
    g.append(list(map(int,input().split())))
    maxV = max(max(g[i]),maxV)# 가장 최댓값
visited = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(L,x,y,total):
    global answer
    if total + (maxV* (4-L))<= answer:# 현재 값+ 남은 가장 최댓값과 합보다 작다면, 그만 두기.
        return
    if L == 4:
        answer = max(answer,total)
        return
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:# 겹치면 안되기에 visited 이용.
            visited[nx][ny] = 1
            dfs(L+1,nx,ny,total+g[nx][ny])
            visited[nx][ny] = 0
            if L == 2:# ㅗ 모양을 만들기 위해서, 다음 좌표를 넘겨줄 때 x,y 그대로 이어간다.
                visited[nx][ny] = 1
                dfs(L+1,x,y,total+g[nx][ny])
                visited[nx][ny] = 0
for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        dfs(1,x,y,g[x][y])
        visited[x][y] = 0

print(answer)
# 백준