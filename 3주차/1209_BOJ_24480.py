from audioop import reverse
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, r = map(int, input().split())
visited = [0]*(n+1)
cnt = 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(r)
for i in range(1, n+1):
    print(visited[i])