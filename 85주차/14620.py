n = int(input())
g = []

for _ in range(n):
    g.append(list(map(int,input().split())))

answer = int(1e9)
visited = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y):
    # x,y 위치에 씨앗이 있을 때, 주변 4곳에 꽃잎이 있는가 체크.
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if visited[nx][ny] == 1:
            return False
    return True

def dfs(L,price,row):
    global answer
    if L == 3:
        answer = min(answer,price)
        return 
    for x in range(row,n-1):
        for y in range(1,n-1):
            if not visited[x][y] and check(x,y):# 씨앗이 있거나 다른 꽃잎이 없는지 체크.
                visited[x][y] = 1
                total = g[x][y]
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    visited[nx][ny] = 1
                    total += g[nx][ny]
                dfs(L+1,price+total,row)
                visited[x][y] = 0# 다시 0을 할당해서 없는 것으로 처리하여 완전탐색 진행!
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    visited[nx][ny] = 0

dfs(0,0,1)
print(answer)
# 백준 꽃길
# 여러분 모두 꽃길 걸으시길 바랍니다!