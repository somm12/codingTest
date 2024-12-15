n = int(input())
L = list(map(int,input().split()))
J = list(map(int,input().split()))

answer = 0
# 완전 탐색 풀이.
def dfs(i, power,joy):
    global answer
    if power <= 0:
        return
    if i == n:
        answer = max(answer,joy)
        return 
    dfs(i+1, power-L[i],joy + J[i])
    dfs(i+1, power,joy)

dfs(0,100,0)
print(answer)
# 백준 안녕
# dp로 푼 풀이.
dp = [0]*101
for i in range(n):
    for j in range(100,L[i],-1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])
print(dp[100])