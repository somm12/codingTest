dp= [[0]*31 for _ in range(31)]# dp를 이용해서 900번 연산으로 값을 구할 수 있다.
def go(W,H):# H와 W의 개수만 알면 구할 수 있음. dp[w][h] = dp[w-1][h+1] + dp[w][h-1].
    if W == 0 and H == 0:# 모두 없어지면 하나의 경우이므로 1반환.
        return 1
    if dp[W][H]:
        return dp[W][H]
    if W > 0:
        dp[W][H] += go(W-1,H+1)
    if H > 0:
        dp[W][H] += go(W,H-1)
    return dp[W][H]

while True:
    n = int(input())
    if n == 0:
        break
    print(go(n,0))
# 백준 알약 문제