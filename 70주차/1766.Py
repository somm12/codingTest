import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = [[] for _ in range(n+1)]

remain = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    remain[b] += 1
q= []
for i in range(1,n+1):
    if remain[i] == 0:# 먼저 풀어야하는 문제가 없는것 부터.
        heapq.heappush(q,i)

answer = []
while q:
    num = heapq.heappop(q)
    answer.append(num)
    for v in g[num]:# 이전에 풀어햐 하는 문제를 풀었으니, 이제 다음으로 풀 수 있는 문제가 된다면, 힙에 넣기.
        if remain[v] > 0:
            remain[v] -= 1
            if remain[v] == 0:
                heapq.heappush(q,v)
for v in answer:
    print(v, end=' ')