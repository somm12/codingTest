from collections import defaultdict
def solution(tickets):
    
    route = defaultdict(list)# 항공권 루트 정보를 담을 dictionary {'ICN':[],,}
    visited = defaultdict(list)# 모든 항공권을 다 써야하므로, 이를 확인할 visited 배열.
    n = len(tickets)
    for a,b in tickets:# dictionary 초기화.
        route[a].append(b)
        visited[a].append(0)
    for key in route:# 경로가 여러 개라면 사전순으로 출력해야하므로 미리 sort.
        route[key].sort()
    total = []
    
    def dfs(res,airport):
        if len(res) == n+1:
            total.append(res)
            return
        for i,next in enumerate(route[airport]):# 현재 공항에서 갈 수 있는 항공권 중에서
            if not visited[airport][i]:# 방문을 하지 않은 경로 선택
                visited[airport][i] = 1
                dfs(res+[next],next)# res 인자를 통해 경로를 저장하고, next:  그 다음 공항 인수로 전달.
                visited[airport][i] = 0 # 백트래킹
    dfs(['ICN'],'ICN')# ICN부터 출발.
    
    return total[0]
# 여행 경로 복습 ok