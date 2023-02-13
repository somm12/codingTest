n = int(input())
dp = [0] * (n+1)

dp[1] = 1

idx2 = 1
idx3 = 1
idx5 = 1
next2 = 2
next3 = 3
next5 = 5

for i in range(2,n+1):
    target = min(next2,next3,next5)
    dp[i] = target
    if target == next2:
        idx2 += 1
        next2 = dp[idx2]*2
    if target == next3:
        idx3 += 1
        next3 = dp[idx3]*3
    if target == next5:
        idx5 += 1
        next5 = dp[idx5]*5
print(dp)