from collections import deque
def solution(n,wires):
    answer = 1000
    g = [[] for _ in range(n+1)]
    
    for a,b in wires:# 그래프 정보 연결하기.
        g[a].append(b)
        g[b].append(a)
    def bfs(start,no):# start 노드 부터 시작해서 탐색했을 때, 해당 네트워크 송전탑 개수 구하기
        q = deque() # no 번 노드는 연결이 끊김.
        q.append(start)
        visited = [0]*(n+1)
        cnt = 0
        visited[start] =1
        while q:
            x = q.popleft()
            cnt += 1
            for nx in g[x]:
                if not visited[nx] and nx != no:
                    visited[nx] = 1
                    q.append(nx)
        return cnt
    
    for a,b in wires:
        cnt = bfs(a,b)
        answer = min(answer, abs(n -(2*cnt)))# 한 덩어리 개수만 알면 나머지 개수는 n-cnt
    
    return answer