import math
from collections import deque
def solution(progresses,speeds):
    answer = []
    n = len(speeds)
    arr = []
    for i in range(n):
        v = math.ceil((100 - progresses[i])/speeds[i])
        arr.append(v)
    stk = []
    q = deque(arr)
    while q:
        if len(stk) == 0:
            v= q.popleft()
            stk.append(v)
        else:
            if q[0] <= stk[0]:
                stk.append(q.popleft())
            else:
                answer.append(len(stk))
                stk = []
        print(stk)
    answer.append(len(stk))
    return answer
# 프로그래머스 큐 파트 문제