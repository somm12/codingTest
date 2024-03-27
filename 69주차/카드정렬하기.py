import heapq
n = int(input())
q = []
for _ in range(n):
    v = int(input())
    heapq.heappush(q,v)
answer=0
while len(q) > 1:
    v1 = heapq.heappop(q)
    v2 = heapq.heappop(q)
    total = v1+v2
    answer += total
    heapq.heappush(q,total)

print(answer)
# 비교 횟수를 최소로 하려면, 그 때 그 때의 최솟값을 구해야함.
