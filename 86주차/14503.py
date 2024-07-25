n,m =map(int,input().split())
x,y,d =map(int,input().split())
dx = [-1,0,1,0]# 북 동 남 서.
dy = [0,1,0,-1]
g = []
tmp =0
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if g[i][j] == 0:
            tmp += 1

answer = 0
visited =[[0]*m for _ in range(n)]
answer =0

while True:
   
    if not visited[x][y]:
        visited[x][y] = 1
        answer += 1
    cnt = 0
    for i in range(4):
        nx,ny =x+dx[i],y+dy[i]
        if not visited[nx][ny] and g[nx][ny] == 0:
            cnt += 1
    if cnt == 0:
        nd = (d+2)%4
        nx,ny = x+dx[nd],y+dy[nd]
        if g[nx][ny] == 0:
            x,y =nx,ny
         
        else:
            break
    else:
        d = (d-1)%4
        nx,ny=x+dx[d],y+dy[d]
        if g[nx][ny] == 0 and not visited[nx][ny]:
            x,y=nx,ny

print(answer)
# 백준 로봇청소기.