n, m = map(int, input().split())
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    arr.append(list(input()))
def dfs(x, y):
    arr[x][y] = '1'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            if arr[nx][ny] == '0':
                dfs(nx, ny)
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            dfs(i,j)
            cnt += 1
print(cnt)
# arr.append(list(map(int,input()))) 정수 01001010 .. 입력 방법.