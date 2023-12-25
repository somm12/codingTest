from collections import deque
n,m = map(int,input().split())
arr = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])

cnt = 0
for v in arr:
    
    if q[0] == v:
        q.popleft()
    else:
        l,r = 0,1# 오른쪽 이동의 경우,왼쪽 이동과 다르게 한 번 더 이동해야함.
        for num in q:
            if num == v:
                break
            l += 1
        for num in list(reversed(q)):
            if num == v:
                break
            r += 1
        if l < r:
            for _ in range(l):
                q.rotate(-1)
            cnt += l
        else:
            for _ in range(r):
                q.rotate(1)
            cnt += r
        q.popleft()
print(cnt)