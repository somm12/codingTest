T = int(input())
def sol(dp,n,m):
    res = -1
    for i in range(1,m):
        for j in range(n):
            if j == 0:
                dp[j][i] += max(dp[j][i-1], dp[j+1][i-1])
            elif j == n - 1:
                dp[j][i] += max(dp[j][i-1], dp[j-1][i-1])
            else:
                dp[j][i] += max(dp[j][i-1], dp[j-1][i-1],dp[j+1][i-1])
    for i in range(n):
        res = max(res, dp[i][m-1])
    return res

for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [a[i:i+m] for i in range(0, len(a), m)] 
    print(sol(dp,n,m))