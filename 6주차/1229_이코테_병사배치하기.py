n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))

# 순서를 뒤집어서 '최장 증가 부분 수열' 문제로 변환(LIS)
# LIS 알고리즘을 이용해서 남은 병사의 수가 최대가 되도록 하는, 열외시킬 병사 수를 구한다.