from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        x = q.popleft()
        cnt = 0
        for i in q:
            if x > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer
# 주식가격    
