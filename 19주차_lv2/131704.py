from collections import deque
def solution(order):
    answer = 0
    q = [i for i in range(1,len(order)+1)]
    q= deque(q)
    second = []
    for i in order:
        if q and i == q[0]:
            q.popleft()
            answer += 1
            
        elif second and second[-1] == i:
            second.pop()
            answer += 1
            
        else:
            while q:
                x = q.popleft()
                second.append(x)
                if x == i:
                    answer += 1
                    second.pop()
                    break
            else:
                return answer
        
    return answer
# 택배상자