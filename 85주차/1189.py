dx = [-1,1,0,0]
dy = [0,0,-1,1]

R,C,k = map(int,input().split())
g = []
for _ in range(R):
    g.append(list(input()))
visited = [[0]*C for _ in range(R)]

visited[R-1][0] = 1
answer = 0

def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

def dfs(x,y):
    if x == 0 and y == C-1:# 도착.
        if visited[0][C-1] == k:# 거리가 k라면 1 반환하여 경우의 수 추가.
            return 1
        return 0
   
    ret = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if inRange(nx,ny) and visited[nx][ny] == 0 and g[nx][ny] == '.':
            visited[nx][ny] = visited[x][y] + 1# 거리 저장
            ret += dfs(nx,ny)# 경우의 수 증가.
            visited[nx][ny] = 0
    
    return ret# 경우의 수 반환.


print(dfs(R-1,0))
# 백준 컴백홈
