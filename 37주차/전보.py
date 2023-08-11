import heapq
INF = int(1e9)
n,m,C = map(int,input().split())
start = C
g = [[]* (n+1) for _ in range(n+1)]# 1 ~ n 번의 각 연결 정보와 비용을 저장할 배열
distance = [INF]*(n+1)# 최대 비용은 INF로 초기화. n까지 최소거리 비용을 저장.

for _ in range(m):# a와 b가 c라는 비용으로 연결됨.
    a,b,c = map(int,input().split())
    g[a].append((b,c))

def di(start):# 다익스트라.
    distance[start] = 0
    q= []
    heapq.heappush(q,(0,start))# (현재 노드까지의 최소 거리, 노드) 형태로 q에 삽입.

    while q:
        dist,now = heapq.heappop(q)# 거리, 노드번호
        if distance[now] < dist:# 이미 이전에 처리된 노드면 continue(이미 앞부분에서 더 빠른 거리로 처리가 되었다면 이 조건이 참이 됨.)
            continue
        for i in g[now]:# 현재 노드와 연결 된 것 중에서
            cost = dist + i[1]# 지금까지의 거리와, now와 연결된 노드 와의 비용을 더한것
            if cost < distance[i[0]]:# distance배열에서 보다 더 적다면 update.
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))# 업데이트 된 부분 q에 삽입.

di(start)
print(distance)
cnt = 0
time = 0
for i,v in enumerate(distance):
    if v != INF:
        cnt += 1 # 도달하는 도시 개수
        time = max(time, v)# 총 걸리는 시간
print(cnt-1,time)# 자기 자신은 빼기.
# 이코테 최단 거리 예제
# 다익스트라.