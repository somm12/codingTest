from collections import defaultdict
        
def solution(tickets):
    answer = []
    dict = defaultdict(list)
    visited = defaultdict(list)
    for a,b in tickets:
        dict[a].append(b)# {'ICN': [xxx,xxxx],,,} 갈 수 있는 경로 딕셔너리 정보 만들기
        visited[a].append(0)# {'ICN':[0,0],,,} 해당 경로에 대한 방문처리 여부를 위한 딕셔너리.
   
    def dfs(airport, route):
        if len(route) == len(tickets)+1:# 경로가 다 만들어지면, answer에 추가
            answer.append(route)
            return
        
        for i,ticket in enumerate(dict[airport]):
            if not visited[airport][i]:
                visited[airport][i] = 1
                dfs(ticket, route+[ticket])# 경로가 정해지면, 해당 공항을 시작으로 가는 티켓을 골라야하므로, 매개변수로 넘겨줌
                visited[airport][i] = 0
    dfs('ICN',['ICN'])
    answer.sort()
    
    return answer[0]
# 프로그래머스 lv3 문제.
# 모든 티켓을 사용하여, 가능한 경로 찾기. 여러 경로라면 사전순.