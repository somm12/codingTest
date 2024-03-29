n = int(input())
dp = [0] * 1000
dp[0] = 1

next2 = 2
next3 = 3
next5 = 5

idx2 = 0
idx3 = 0
idx5 = 0

for i in range(1,n):
    dp[i] = min(next2,next3,next5)
    if dp[i] == next2:
        idx2 += 1
        next2 = dp[idx2] * 2
    if dp[i] == next3:
        idx3 += 1
        next3 = dp[idx3] * 3
    if dp[i] == next5:
        idx5 += 1
        next5 = dp[idx5] * 5
print(dp[n-1])