import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(n1,n2):
    q = deque()
    q.append((n1,0))
    q.append((n2,0))
    visit = [0]*(n+1)
    visit[n1] = 1
    visit[n2] = 1
    total = 0
    while q:
        node,dist = q.popleft()
        total += (dist * 2)
        for v in g[node]:
            if not visit[v]:
                visit[v] =1
                q.append((v,dist+1))
    return total


cand = []

for n1 in range(1,n+1):# 두 곳 고르기.
    for n2 in range(n1+1,n+1):
        time = bfs(n1,n2)# 최소왕복시간 합 구하기.
        cand.append([n1,n2,time])

cand.sort(key = lambda x:(x[2],x[0],x[1]))# 가장 왕복 시간 합이 작고, 건물번호작은 순.

for v in cand[0]:
    print(v,end = ' ')
#호석이 두마리 치킨 

# 플로이드 웨셜 방법으로 풀기
import sys
n, m = map(int, sys.stdin.readline().split()) 
INF = int(1e9)

g = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a][b] = 1
    g[b][a] = 1

# 자기 자신 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            g[a][b] = 0

# 모든 정점에서 모든 정점으로 가는 최소 거리
for k in range(1, n + 1):# 거쳐가는 노드.
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])

# 2개의 건물 고르기,모든 집을 방문해서 걸리는 더 최소 거리를 측정 
min_sum = INF
result = list()
for i in range(1, n+1):  # 건물 2개를 뽑는다.
    for j in range(i+1, n + 1):
        sum_ = 0
        for k in range(1, n + 1):  # 모든 집을 방문하면서 거리를 측정
            sum_ += min(g[k][i], g[k][j]) * 2  # k -> i, k -> j 중에 짧은 거리 합치기
        if sum_ < min_sum:
            min_sum = sum_
            result = [i, j, sum_]

print(*result)
# 백준