def solution(n):
    answer = 0
    dp = [0]*(n+1)
    for i in range(1,n+1):
        if i <= 2:
            dp[i] = i
        else:
            dp[i] = (dp[i-1]+dp[i-2])%1000000007
    return dp[n]
# 2 x n 타일링