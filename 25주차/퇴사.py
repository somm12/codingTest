n = int(input())
T = [0]
P = [0]
# index는 1부터.
dp = [0]*(n+2) # i + t[i] == n+1 일 때도 해당 금액이 포함되야하므로 n+1개가 필요.
# i가 8일이고 t[i]가 3이며, n 이 10일 때, 8 9 10 이라 금액이 포함될 수 있다. dp[n+1]에 이를 반영.
for _ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
# dp[i]는 i일 까지 받을 수 있는 최대 금액.
for i in range(1,n+1):# dp[n+1]까지 포함!
    for j in range(i + T[i], n+2): # 적어도 i + T[i] 일 부터 n일 까지는 dp[i] + P[i] 금액을 얻을 수 있음.
        dp[j] = max(dp[i] + P[i], dp[j])
print(max(dp))
