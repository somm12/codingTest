from collections import deque
n,m,k,x = map(int,input().split())

distance = [0]*(n+1)

g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)

def bfs(start):# 출발점을 중점으로 탐색하기. 뻗어나갈 수록 이전 노드 +1 씩 거리가 늘어남.
    visited = [0]*(n+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for v in g[now]:
            if not visited[v]:
                visited[v] = 1
                q.append(v)
                distance[v] = distance[now] + 1
bfs(x)
arr = []
for i in range(1,n+1):
    if distance[i] == k:# 거리가 k인 노드 추가.
        arr.append(i)
if len(arr) == 0:# 없으면 이면 -1.
    print(-1)
else:
    for v in arr:
        print(v)

# 이코테 bfs/dfs 문제.