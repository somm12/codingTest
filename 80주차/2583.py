import sys
sys.setrecursionlimit(10*10000)

n,m,k=map(int,input().split())
g = [[1]*m for _ in range(n)]
for _ in range(k):
    a,b,c,d = map(int,input().split())
    a,b = b,a
    c,d =d,c
    for x in range(a,c):
        for y in range(b,d):
            g[x][y] = 0

arr =[]
visited =[[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,cnt):# dfs로 면적 넓이 찾기.

    visited[x][y] = 1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == 1:
            cnt = dfs(nx,ny,cnt+1)# 끝까지 재귀를 하면서 반환되는 값 cnt를 업데이트하여, 이어서 넓이를 구할 수 있게 한다.
    return cnt

for x in range(n):
    for y in range(m):
        if g[x][y] == 1 and not visited[x][y]:
            
            arr.append(dfs(x,y,1))

print(len(arr))

arr.sort()
for v in arr:
    print(v,end=' ')
# 백준 영역 구하기