import sys
input = sys.stdin.readline
INF = int(1e9)
graph = []
n = int(input().rstrip())
m = int(input().rstrip())
for _ in range(n):
    graph.append(list(map(int,input().split())))
route = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

res = "YES"
for i in range(m-1):
    if graph[route[i]-1][route[i+1]-1] >= INF and route[i] != route[i+1]:
        
        res = "NO"
        break
print(res)
# 노드 간 연결 확인 문제에서 
# 플로이드 와샬을 활용하므로, route[i] != route[i+1] 부분은 자기자신은 연결되어 있다는 뜻.