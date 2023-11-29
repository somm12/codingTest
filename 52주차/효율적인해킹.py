import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
g = [[] for _ in range(n+1)]
answer =[]
for _ in range(m):
    a,b = map(int,input().split())
    g[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0]*(n+1)
    visited[start] = 1
    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for i in g[v]:
            if not visited[i]:
                visited[i]=1
                q.append(i)
    return cnt

for i in range(1,n+1):
    answer.append([i, bfs(i)])
answer.sort(key=lambda x: (-x[1],x[0]))
maxV = answer[0][1]

for v in answer:
    if v[1] == maxV:
        print(v[0],end=' ')
    else:
        break
# 백준 그래프 탐색.