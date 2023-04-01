import heapq
def dj(start,graph,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
        
def solution(N, road, K):
    answer = 0
    INF=int(1e9)
    distance = [INF]*(N+1)
    g = [[] for _ in range(N+1)]
    for a,b,c in road:
        g[a].append((b,c))
        g[b].append((a,c))
    dj(1,g,distance)
    for i in distance:
        if i <= K:
            answer += 1
    return answer
# 배달
# 다익스트라 알고리즘 - 최단경로