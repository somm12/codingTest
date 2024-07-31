import sys
sys.setrecursionlimit(1000+1)
input = sys.stdin.readline
tc = int(input())
def dfs(start):
    visited[start] = 1
    for nxt in g[start]:
        if not visited[nxt]:
            dfs(nxt)
            
def counting():
    cnt = 0
    for start in range(1,n+1):
        if not visited[start]:
            dfs(start)
            cnt += 1
    return cnt 

for _ in range(tc):
    n = int(input())
    answer ='tree'
    m = int(input())
    g = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)

    visited =[0]*(n+1)
    cnt = counting()
    if cnt > 1:
        answer = 'graph'
    if n-1 != m:
        answer = 'graph'
    print(answer)
# 트리는 항상 n-1 =m (간선의 개수 == 노드의 개수 -1)
# 노드들이 하나로 연결되어있다.
# 백준 Tree