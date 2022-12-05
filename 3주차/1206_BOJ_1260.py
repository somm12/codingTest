from collections import deque
import sys 
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n + 1):
    graph[i].sort()

visited = [False] * (n + 1)

def dfs(v):
    print(v, end = ' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        s = q.popleft()
        print(s, end= ' ')
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)