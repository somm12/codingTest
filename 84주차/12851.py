from collections import deque
n,k =map(int,input().split())
MAX = 100000
def bfs(x):
    visited = [0]*(MAX+1)# 최대 범위는 10만이기 때문에,
    q = deque()
    q.append(x)

    cnt = [0] * (MAX+1)
    cnt[x] = 1 # 최단거리로 해당 정점까지 갈 수 있는 방법의 수 저장.
    visited[x] = 1 # 방문처리 체크 겸 + 최단 거리 시간 저장.
    if n == k:
        return [0,1]
    while q:
        x = q.popleft()
        for v in [x-1,x+1,2*x]:
            if 0<= v <= MAX:
                if not visited[v]:# 방문이 처음일 때.
                    q.append(v)
                    visited[v] = visited[x] + 1# 걸리는시간 + 1
                    cnt[v] += cnt[x]# 경우의 수 추가. 이전 정점에서 그대로 더해짐.
                elif visited[v] == visited[x] + 1:# 최단거리에 해당 할 때, 개수 추가.
                    cnt[v] += cnt[x]
        
    return [visited[k] - 1,cnt[k]]

a,b = bfs(n)
print(a)
print(b)
# 백준 숨바꼭질 2.