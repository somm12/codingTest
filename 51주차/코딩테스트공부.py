import heapq
def solution(alp, cop, problems):
    INF = int(1e9)
    # 알고력 1 증가 문제, 코딩력 1 증가 문제가 추가 되었다고 치기
    problems += [[0,0,1,0,1], [0,0,0,1,1]]
    problems.sort() # 알고력이 적은 것 부터 정렬.
    max_alp = problems[-1][0] # 가장 큰, 즉 목표로 하는 알고력과 코딩력 구하기
    max_cop = 0
    for _,v,_,_,_ in problems:
        max_cop = max(max_cop, v)
    # distance[alp][cop]: 각 alp과 cop 까지 오는 데 걸린 최소시간을 담을 배열 
    distance = [[INF] *(max_cop+1) for _ in range(max_alp+1)]
    # 혹시 초기 값이 이미 목표치 보다 클 때, index out of range를 피하기 위함.
    alp = min(alp, max_alp)
    cop = min(cop,max_cop)
    distance[alp][cop] =0# 첫 출발점은 걸린 시간 0
    q = []
    heapq.heappush(q,[0,alp,cop])# 최단 시간 순으로 정렬 되도록.
    while q:
        dist,alp,cop = heapq.heappop(q)
        if distance[alp][cop] < dist:# 이미 최단시간이라면 패스.
            continue
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp < alp_req or cop < cop_req:# 둘 중 하나가 부족 하다면, 넘기기
                if alp < alp_req and cop < cop_req:# 둘 다 부족하면 더 볼 필요없이 break. 큐에 남은거 이어서 실행.
                    break
                continue
            # 해당 문제를 풀었을 때 얻을 알고력과 코딩력. 이미 최대 치를 넘을 수 있기에 에러가 나지 않도록 min값을 구함.
            nxt_alp = min(max_alp, alp+alp_rwd)
            nxt_cop = min(max_cop, cop+cop_rwd)
            
            if distance[nxt_alp][nxt_cop] > cost+dist:# 이문제 푸는데 드는 시간+ 지금까지 시간이 더 적게 걸리면 업데이트.
                distance[nxt_alp][nxt_cop] = cost+dist
                heapq.heappush(q,[cost+dist, nxt_alp, nxt_cop])
                
                
   
    return distance[max_alp][max_cop]# 목표치 알고력과 코딩력까지 걸린 최단 시간
# 프로그래머스. 
# 다익스트라 활용해서 풀기.