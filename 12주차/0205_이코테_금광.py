import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    dp = [[0]*m for _ in range(n)]
    arr = list(map(int,input().split()))
    g = []
    ans = 0
    for i in range(0,n*m,m):
        g.append(arr[i:i+m])
    for i in range(n):
        dp[i][0] = g[i][0]
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                dp[i][j] = g[i][j] + max(dp[i][j-1],dp[i+1][j-1])
            elif i == n-1:
                dp[i][j] = g[i][j] + max(dp[i][j-1],dp[i-1][j-1])
            else:
                dp[i][j] = g[i][j] + max(dp[i][j-1],dp[i+1][j-1],dp[i-1][j-1])
    for i in range(n):
        ans = max(ans,dp[i][m-1])
    print(ans)

