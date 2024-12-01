n = int(input())
g = [[0]*(n+2) for _ in range(n+2)]
arr =[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

for x in range(n):
    for y in range(n):
        g[x+1][y+1] = arr[x][y]

dp = [[[0]*3 for _ in range(n+2)] for _ in range(n+2)]
dp[1][2][0] = 1

# x,y 끝 지점을 기준으로 d방향의 파이프가 일 때, 벽이 있는지 체크하는 함수
def check(x,y,d):# 벽이 있는지 체크. 범위는 체크 안해도 된다.(2차원 배열의 범위를 18까지 넓혔기 때문에 범위 초과는 신경쓰지 않아도 됨.)
    if d == 0 or d == 2: # 가로 또는 세로 방향
        if g[x][y] == 0:
            return True
        return False
    else:# 대각선
        if g[x][y] == 0 and g[x-1][y] == 0 and g[x][y-1] == 0:
            return True
        return False

for i in range(1,n+1):
    for j in range(1,n+1):
        if check(i,j+1,0):# 가로 방향에서 가로로 한 칸 이동.
            dp[i][j+1][0] += dp[i][j][0]
        if check(i+1,j+1,1):# 가로 방향에서 대각선 한 칸 이동
            dp[i+1][j+1][1] += dp[i][j][0]
        
        # 세로 방향에서
        if check(i+1,j+1,1):# 대각선으로 이동
            dp[i+1][j+1][1] += dp[i][j][2]
        if check(i+1,j,2):# 세로로 이동 
            dp[i+1][j][2] += dp[i][j][2]
        
        # 대각선 방향에서
        if check(i,j+1,0):# 가로로 이동.
            dp[i][j+1][0] += dp[i][j][1]
        if check(i+1,j+1,1):# 대각선으로 이동.
            dp[i+1][j+1][1]+= dp[i][j][1]
        if check(i+1,j,2):# 세로로 이동
            dp[i+1][j][2] += dp[i][j][1]

print(dp[n][n][0] + dp[n][n][1] + dp[n][n][2])
# 백준 파이프 옮기기