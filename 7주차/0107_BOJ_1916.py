import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

x,y = map(int, input().split())

def da(start, end):
    q= []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    print(distance[end])

da(x,y)

