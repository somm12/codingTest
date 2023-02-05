import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    a = list(map(int,input().split()))
    dp.append(a)
for x in range(1,n):
    for y in range(x+1):
        if y == 0:
            dp[x][y] += dp[x-1][y]
        elif x == y:
            dp[x][y] += dp[x-1][y-1]
        else:
            dp[x][y] += max(dp[x-1][y-1],dp[x-1][y])
print(max(dp[n-1]))