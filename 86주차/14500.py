n,m = map(int,input().split())
g = []
maxV = 0
for i in range(n):
    g.append(list(map(int,input().split())))
    maxV = max(maxV, max(g[i]))

answer=0
visited = [[0]*m for _ in range(n)]
dx =[-1, 1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x< n and 0 <= y < m
def dfs(L,x,y,total):
    global answer
    
    if L == 4:
        answer = max(answer,total)
        return 
    if total + (maxV * (4-L)) <= answer:# 가장 최댓값으로 계산해도 answer보다 이하면 더이상 재귀를 멈춰되 됨.
        return
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if inRange(nx,ny) and not visited[nx][ny]:
            if L == 2:# 2번째 칸 까지 왔을 때, ㅏ 모양 만들려면 nx,ny로 넘어가지 않고 그대로 이어간다. 
                visited[nx][ny] = 1
                dfs(L+1,x,y,total+g[nx][ny])
                dfs(L+1,nx,ny,total+g[nx][ny])
                visited[nx][ny] = 0
            else:# 아닌 경우는 4방향 중 하나로 이어가기.
                visited[nx][ny] = 1
                dfs(L+1,nx,ny,total+g[nx][ny])
                visited[nx][ny] = 0
            
for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        dfs(1,x,y,g[x][y])
        visited[x][y] = 0

print(answer)
# 백준 테르노미노.