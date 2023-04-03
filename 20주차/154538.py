from collections import deque
def solution(x, y, n):
    q = deque()
    q.append(x)
    dist = [0]*(10**6+1)
    while q:
        x = q.popleft()
        if x == y:
            return dist[x]
        for v in [x*2,x*3,x+n]:
            if v <= y and not dist[v]:
                q.append(v)
                dist[v] = dist[x] + 1
            
    return -1
# 숫자 변환하기 복습.