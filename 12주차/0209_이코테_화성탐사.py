import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(x,y,n,g):
    q = []
    distance = [[INF] * n for _ in range(n)]
    heapq.heappush(q,(g[x][y],(x,y)))
    distance[x][y] = g[x][y]
    while q:
        dist, (x,y) = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] < dist:
                    continue
                cost = dist + g[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,(nx,ny)))
    return distance[n-1][n-1]

for _ in range(T):
    n = int(input())
    g = []
    for _ in range(n):
        g.append(list(map(int,input().split())))
    res = solution(0,0,n,g)
    print(res)