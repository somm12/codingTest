from collections import deque
def solution(x, y, n):
    answer = -1
    q = deque()
    q.append(x)
    dist = [0]*(10**6 + 1)
    while q:
        x = q.popleft()
        if x == y:
            return dist[x]
        for i in [x*2,x*3,x+n]:
            if i <= 10**6 and not dist[i]:
                q.append(i)
                dist[i] = dist[x] + 1
        
    return answer
# 숫자 변환하기