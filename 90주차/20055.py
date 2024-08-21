from collections import deque

n,k = map(int,input().split())
q= deque()

for v in list(map(int,input().split())):
    q.append([0,v])

nth = 1
cnt = 0
while True:
    # 벨트 회전.
    q.appendleft(q.pop())
    if q[n-1][0]:# 즉시 내리는 위치 확인.
        q[n-1][0] = 0
    # 로봇들의 이동.
    for i in range(n-2,-1,-1):
        if q[i][0] and q[i+1][0] == 0 and q[i+1][1] >= 1:
            q[i+1][0] = 1
            q[i+1][1] -= 1
            q[i][0] = 0
            if q[i+1][1] == 0:# 혹시 내구도가 0이되면 체크.
                cnt += 1
            
          
    if q[n-1][0]:# 이동 후에, 내리는 위치 확인.
        q[n-1][0] = 0
    
    if q[0][1] >= 1:# 로봇올리기.
        q[0][1] -= 1
        q[0][0] = 1
        if q[0][1] == 0:
            cnt += 1
    
    if cnt >= k:#K개이상 내구도 0이면 종료.
        break
    nth += 1

print(nth)
# 백준 컨베이어 벨트 위 로봇.