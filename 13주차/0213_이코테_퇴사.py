n = int(input())
t = [0]
p = [0]
dp = [0] * (n+1)
for _ in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n,0,-1):
    if i + t[i] <= n:
        for j in range(i,n+1):
            if i + t[i] <=j:
                dp[i] = max(dp[i],p[i]+dp[j])
    elif i + t[i] == n+1:
        dp[i] = p[i]

print(max(dp))

