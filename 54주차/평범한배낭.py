n,k = map(int,input().split())

arr = [[]]
for _ in range(n):
    w,v = map(int,input().split())
    arr.append([w,v])
dp = [[0]*(k+1) for _ in range(n+1)]# n번째 가방까지 포함할 때, 가방 제한 무게가 k일때 최대 가치.

for i in range(1,n+1):
    w,v = arr[i]# 현재 가방 무게와 가치
    for j in range(1,k+1):# 1~k까지 가방 제한 무게
        if j < w:# 가방 제한 무게가 현재 가방보다 작으면, 현재 가방 포함X.
            dp[i][j] = dp[i-1][j]
        else:# 현재 가방을 포함하지 X or 현재 가방을 포함함( 현재 가방무게를 포함하기 이전의 가치 + 현재 가방 가치. )
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])
# 백준 문제