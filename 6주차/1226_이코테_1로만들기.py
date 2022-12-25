n = int(input())
dp = [0] * (n+1)

for i in range(2,n+1):
    res = 100000
    if i % 5 == 0:
        res = min(res,dp[i//5] + 1)
    if i % 3 == 0:
        res = min(dp[i//3] + 1,res)
    if i % 2 == 0:
        res = min(dp[i//2] + 1,res)
    
    res = min(res,dp[i-1] + 1)
    dp[i] = res
print(dp[n])