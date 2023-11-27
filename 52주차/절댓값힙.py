import heapq
import sys
q = []
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q,(abs(x),x))
    else:
        if len(q) == 0:
            print(0)
        else:
            _,v = heapq.heappop(q)
            print(v)
# 백준 자료구조