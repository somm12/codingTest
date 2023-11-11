from collections import deque
def solution(q1,q2):
    answer = 0
    q1 = deque(q1)
    q2 = deque(q2)
    cycle = (len(q1) + len(q2))*2
    
    q1Total = sum(q1)
    q2Total = sum(q2)
    target = q1Total + q2Total
    if target % 2 !=0:
        return -1
    target = target//2
    
    while True:
        if cycle < answer:
            return -1
        if q1Total == q2Total:
            return answer
        if q1Total > target:
            v = q1.popleft()
            q2.append(v)
            q1Total -= v
            q2Total += v
        else:
            v = q2.popleft()
            q1.append(v)
            q2Total -= v
            q1Total += v
        answer += 1
# 큐에서 직접 pop, insert해서 풀기.