from pydoc import visiblename
import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [0]* (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[v] + 1
                q.append(i)
bfs(x)
res = 0
for i in range(1,n+1):
    if dist[i] == k:
        res += 1
        print(i)
if res == 0:
    print(-1)
