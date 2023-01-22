import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i + 1 ,n):
        if arr[i] != arr[j]:
            cnt += 1
print(cnt)

# 더 효과적인 방법
n, m = map(int,input().split())
arr = list(map(int, input().split()))
w = [0] * 11
for data in arr:
    w[data] += 1
total = n
res = 0
for i in range(1,m+1):
    total -= w[i]
    res += (w[i] * total)