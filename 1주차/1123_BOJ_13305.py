import sys
input = sys.stdin.readline
n = int(input())
size = list(map(int, input().split()))
p = list(map(int, input().split()))
res = 0
minp = (10 ** 9)

for i in range(n - 1):
    if minp > p[i]:
        res += p[i] * size[i]
        minp = p[i]
    else:
        res += minp * size[i]

print(res)