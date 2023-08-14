from collections import deque
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])# 짧은 비용 순으로 정렬.
    g = [[] for _ in range(n)]
    def isConnected(a,b):# a,b가 연결이 되어있는지 확인
        q = deque([a])
        visited = [0]*n
        visited[a] = 1
        flag = False
        while q:
            v = q.popleft()
            if v == b:
                flag = True
            for i in g[v]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
        return flag
                    
    for a,b,cost in costs:
        if isConnected(a,b):
            continue
        else:# 연결이 되어있지 않다면 연결시키고, 비용 추가
            answer += cost
            g[a].append(b)
            g[b].append(a)
    return answer
# 프로그래머스 lv3 문제