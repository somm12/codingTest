n,k =map(int,input().split())
dp = [0] *(k+1)
for _ in range(n):
    w,v = map(int,input().split())
    for i in range(k,w-1,-1):# 뒤쪽부터 최대 가치를 계산해나가면, 물건을 하나씩 사용하는 걸로 할 수 있음. 
        dp[i] = max(dp[i-w] + v , dp[i])

print(dp[k])
# 백준 평범한 배낭.