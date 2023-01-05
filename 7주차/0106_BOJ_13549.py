import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, k = map(int, input().split())
graph = [[] for _ in range(100001)]
distance = [INF] * (100001)

def da(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            continue
       
        for i in [(now+1,1),(now-1,1),(now*2,0)]:
            cost = dist + i[1]
            if 0 <= i[0] < 100001 and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    print(distance[k])
da(n)

# 그래프 입력이 받는 것이 아닌, 세 방향을 중심으로 이동 + 해당 좌표는 범위가 제한 됨. 포인트!

