import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = [0]*n
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    if i + arr[i][0] <= n:
        dp[i] = arr[i][1]
        for j in range(i):
            if j + arr[j][0] <= i:
                dp[i] = max(dp[i],arr[i][1] + dp[j])
print(max(dp))