import sys
input = sys.stdin.readline
n, m = map(int, input().split())
card = []

for _ in range(n):
    card.append(list(map(int, input().split())))
maxV = -1e9

for li in card:
    maxV = max(min(li), maxV)
print(maxV)
# 각행에서 가장 작은 숫자들 중 제일 큰 수 구하기.
