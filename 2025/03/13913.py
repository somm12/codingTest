from collections import deque

n,k = map(int,input().split())
maxV  = 100000
minV = 0
visited = [0]*(maxV+1)
record = [0] * (maxV+1)

def bfs(start):
    q= deque()
    q.append(start)
    visited[start] = 1
    record[start] = start
    while q:
        x = q.popleft()
        for nxt in [2*x, x+1,x-1]:
            if minV <= nxt <= maxV:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = visited[x] + 1
                    record[nxt] = x
                    if nxt == k:
                        return
bfs(n)
ans = []
t = k
while True:
    if t == n:
        break
    value =record[t]
    ans.append(value)
    t= value

ans.reverse()
ans.append(k)
print(visited[k] - 1)
for v in ans:
    print(v,end=" ")
# 백준 숨바꼭질4