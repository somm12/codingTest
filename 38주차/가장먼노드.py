from collections import deque
def solution(n, edge):
    answer = 0
    g = [[] for _ in range(n+1)]
    distance =[0]*(n+1)
    for a,b in edge:
        g[a].append(b)
        g[b].append(a)
    def bfs():
        q= deque()
        visited = [0]*(n+1)
        visited[1] = 1
        q.append(1)
        while q:
            now = q.popleft()
            for v in g[now]:
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
                    distance[v] = distance[now] + 1
    bfs()
    
    maxV = max(distance)
    answer = distance.count(maxV)

    return answer

# 프로그래머스 lv3문제
# 최단 경로: 가중치가 없다면 bfs 가능, 가중치가 있다면 다익스트라.