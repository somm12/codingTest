import heapq
import sys
input = sys.stdin.readline

N,E = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
x, y = map(int, input().split())
def da(start):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return distance
d = da(1)
f = da(x)
g = da(y)
res = min(d[x] + f[y] + g[N], d[y] + g[x] + f[N])
if res >= INF:
    print(-1)
else:
    print(res)
