INF = int(1e9)
n, m = map(int ,input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n + 1):
    graph[i][i] = 0

x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
res = graph[1][k] + graph[k][x]

if res >= INF:
    print(-1)
else:
    print(res)
# 양방향으로 이동가능한 것을 놓치지말기
# k를 거쳐서 이동할 수 있는 최소 시간. 플로이드 워샬 알고리즘을 이용한다.