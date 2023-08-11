n,m = map(int,input().split())
INF = int(1e9)
g = [ [INF]* (n+1) for _ in range(n+1)]
for i in range(1,n+1): 
    g[i][i] = 1

for _ in range(m):
    a,b = map(int,input().split())
    g[a][b]=1
    g[b][a] = 1


x,k = map(int,input().split())
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            g[a][b] = min(g[a][b], g[a][i]+g[i][b])
for i in g:
    print(i)
answer = g[1][k] + g[k][x]
if answer >= INF:
    print(-1)
else:
    print(answer)

# 이코테 최단경로 예제 문제
# 양방향 연결. 1->k->x 최소 걸리는 시간 구하기.
# 입력 크기는 100 이하.
# 플로이드 워셜 문제. a->b로 가는 경로는 k를 거쳐서 가는 경로 비용들 중 최소 찾기
# min(D(ab)) = min(D(ab), D(ak)+D(kb))