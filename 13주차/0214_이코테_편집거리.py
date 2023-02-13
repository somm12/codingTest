a = input()
b = input()

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(len(b)+1):
    dp[0][i] = i
for i in range(len(a)+1):
    dp[i][0] = i

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
print(dp[len(a)][len(b)])