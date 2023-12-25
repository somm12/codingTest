from collections import deque
n,w,L = map(int,input().split())
q = deque(list(map(int,input().split())))
b = deque([0]*w)#다리
t = 0
total = 0# 다리 위의 트럭들의 총 무게
cnt = 0# 다리 위에 올라간 트럭 총 개수.

while total > 0 or q:# 다리 위에 트럭이 아직 있거나, 대기 중인 트럭이 있는 경우 반복.
    out = b.popleft()
    if out > 0:# 빠져나간 트럭이 있는 경우.
        total -= out
        cnt -= 1
    if q and total+q[0] <= L and cnt + 1 <= w:# 대기 중인 트럭이 있고, 무게와 개수가 제한 내라면 pop
        v = q.popleft()
        b.append(v)
        total += v
        cnt += 1
    else:# 아니라면, 다시 0으로 append해서 채우기
        b.append(0)
    t += 1
   
print(t)