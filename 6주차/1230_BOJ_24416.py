n = int(input())
cnt = 0

def fib2(n):
    global cnt
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt += 1
    return dp[n]


print(fib2(n), cnt)
# 재귀로 푼 횟수가 n번째 피보나치수와 같다.