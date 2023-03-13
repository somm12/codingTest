def solution(n):
    dp = [0] * (n+1)
    for i in range(1,n+1):
        if i <= 2:
            dp[i] = i
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]
# 멀리 뛰기