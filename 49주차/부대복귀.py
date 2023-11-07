from collections import defaultdict,deque

def solution(n, roads, sources, dest):
    answer = []
    dict = defaultdict(list)
    for a,b in roads:
        dict[a].append(b)
        dict[b].append(a)
        
    INF = int(1e9)
    def bfs(start):
        q = deque()
        
        q.append((start,0))
        distance = [INF]*(n+1)
        distance[start] = 0
        while q:
            now,dist = q.popleft()
            if distance[now] < dist:
                continue
                
            for i in dict[now]:
                cost = dist+1
                if cost < distance[i]:
                    distance[i] = cost
                    q.append((i, cost))
                
        return distance           
    arr = bfs(dest)
    for v in sources:
        if arr[v] != INF:
            answer.append(arr[v])
        else:
            answer.append(-1)# 갈 수 없다면 -1.
    return answer
# 모든 거리가 1이므로 bfs로 대체 가능
# 여러 출발 지점에서 부터, 같은 도착지점까지의 거리를 알면 되므로, 
# 도착지점 중심의 다익스트라 구하기.
# 프로그래머스