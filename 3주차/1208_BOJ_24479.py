import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
cnt = 0
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

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


# n이 10,0000 & m이 20,0000 입력.
# readline, sys.setrecursionlimit 사용이 핵심.