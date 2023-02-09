import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
distance[0] = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def da(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
da(1)
res = 30000
cnt = 0 
d = max(distance)
for i in range(1,n+1):
    if distance[i] == d:
        res = min(res,i)
        cnt += 1
print(res,d,cnt)