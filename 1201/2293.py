n,k = map(int,input().split())
dp = [0]*(k+1)
dp[0] = 1# 아무 것도 없다는 의미 그 자체로 1.
for _ in range(n):
    value = int(input())
    for i in range(value, k+1):
        dp[i] += dp[i-value] 
# 원래 경우의 수 + i-value 라는 수를 만드는데 경우의 수 더하기. i가 4일 때, value가 2라면, dp[2] + dp[4] (i-value 제외한 경우의 수만 찾으면 됨)
print(dp[k])
# 백준 동전1