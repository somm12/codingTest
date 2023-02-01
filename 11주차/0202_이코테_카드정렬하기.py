import sys
import heapq
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q,int(input()))

result = 0
while len(q) != 1:
    one = heapq.heappop(q)
    two = heapq.heappop(q)
    v = one + two
    result += v
    heapq.heappush(q,v)

print(result)