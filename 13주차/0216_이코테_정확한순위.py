n, m = map(int,input().split())
INF = int(1e9)
g = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    g[i][i] = 0

for _ in range(m):
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1

for k in range(1,n+1):
    for u in range(1,n+1):
        for j in range(1,n+1):
            g[i][j] = min(g[i][j],g[i][k] + g[k][j])


cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if g[i][j] == INF:
            break
    else:
        cnt += 1
print(cnt)