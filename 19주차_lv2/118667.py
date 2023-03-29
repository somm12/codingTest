from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    max_cnt = len(q1) * 4
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while sum1 != sum2:
        if answer > max_cnt:
            return -1
        if not q1 or not q2:
            return -1
        if sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x
        answer += 1
    return answer
# 두 큐 합 같게 만들기.