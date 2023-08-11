import heapq
INF = int(1e9)
n,m,k,x = map(int,input().split())

g = [ []*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append((b,1))

distance = [INF]*(n+1)

def di(start):
    distance[start] = 0
    q= []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in g[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                
                heapq.heappush(q,(cost, i[0]))
di(x)

cnt =0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)

# 백준 최단 거리 문제
# x에서 출발해서, 최단거리가 k인 번호들을 출력. 없다면 -1 출력.