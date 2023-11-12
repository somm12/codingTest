import heapq
def solution(n, paths, gates, summits):
    answer = []
    summ = set()
    for v in summits:
        summ.add(v)
    g= [[] for _ in range(n+1)]
    for a,b,c in paths:
        g[a].append((b,c))
        g[b].append((a,c))
        
    INF = int(1e9)
    intens = [INF]*(n+1)
    def da():
        q = []
        # 모든 지점에서의 최소의 Intensity를 구하면 되므로, 모든 시작점 부터 heap에 넣기.
        for gate in gates:
            heapq.heappush(q,(0,gate))
            intens[gate] = 0 
        
        while q:
            intensity,now = heapq.heappop(q)
            # 봉우리 도착 하거나 현재 노드까지의 intensity가 이미 작은 값이면 그만.
            if now in summ or intens[now] < intensity:
                continue
            
            for next,weight in g[now]:
                newInten = max(intensity, weight)# 다음 경로에서의 최대 intensity.
                if newInten < intens[next]:# 더작은 값이라면 그 값으로 업데이트.
                    intens[next] = newInten
                    heapq.heappush(q,(newInten,next))
        return intens
    
    da()
    for v in summits:
        answer.append((v,intens[v]))
    
    answer.sort(key=lambda x: (x[1],x[0]))
    

    return [answer[0][0],answer[0][1]]
# 다익스트라 응용 문제
# 현재 노드까지의 최소 거리 합이 기준이 아닌, 현재 노드까지의 모든 경로들 중 최대 비용 값이 기준.
# 최소의 intensity를 구해야 하므로, heap 이용.
# 프로그래머스 문제