import heapq
import sys
from turtle import distance
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int , input().split())
graph = [[] for _ in range(n + 1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b, k = map(int, input().split())
    graph[a].append((b,k))

def d(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
d(c)
res = -1
cnt = 0
for i in range(1, n + 1):
    if distance[i] != INF:
        cnt += 1
        res = max(res, distance[i])

print(cnt-1, res)# 자기자신 제외