

import heapq


t = int(input())

INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def da(g):
    distance = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q,(g[0][0],(0,0)))
    distance[0][0] = g[0][0]
    while q:
        dist,(x,y) = heapq.heappop(q)
        if x == n-1 and y == n-1:
            return distance[x][y]
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + g[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,(nx,ny)))
for _ in range(t):
    n = int(input())
    g = []
    for _ in range(n):
        g.append(list(map(int,input().split())))
    print(da(g))

