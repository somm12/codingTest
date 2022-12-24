n = int(input())
arr = list(map(int, input().split()))
dp = [0]*100
dp[0] = arr[0]
dp[1] = max(arr[0],arr[1 ])
for i in range(2, n):
    dp[i] = max(dp[i - 1],dp[i - 2] + arr[i])

print(dp[n-1])

# i-1번째 식량창고 털기 + i번째 털 수 없음
# i-2번째 식량창고 털기 + i번째 창고 털 수 있음.
# i번재 창고를 털지 말지에 대해서 2가지 경우(위의 2가지)로 문제 해결 가능.