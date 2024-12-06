n,k = map(int,input().split())
INF = int(1e9)
dp = [INF]*(k+1)
dp[0] = 0
for _ in range(n):
    value = int(input())
    for i in range(value, k+1):
        dp[i] = min(dp[i], dp[i - value] + 1)# 여러번 동전 사용가능 하므로, 현재 동전 금액을 빼서 이전 최소 값 + 현재 금액( +1 역할)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
# 백준 동전2