from collections import deque

n,k = map(int,input().split())
maxV = 100000
minV = 0
cnt = 0
visited = [0] * (maxV + 1)
cnt = [0] * (maxV + 1)
def bfs(start):
    q = deque()
    q.append(n)
    visited[start] = 1
    cnt[start] = 1
    while q:
        now = q.popleft()
        for nxt in [now*2, now+1,now-1]:
            if minV <= nxt <= maxV:
                if not visited[nxt]:
                    visited[nxt] = visited[now] + 1 # 가지수
                    q.append(nxt)
                    cnt[nxt] += cnt[now]# 경우의 수.
                elif visited[nxt] == visited[now] + 1:
                    cnt[nxt] += cnt[now]
                    
                    

bfs(n)
print(visited[k] - 1)
print(cnt[k])
# 백준 숨바꼭질2