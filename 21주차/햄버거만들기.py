from collections import deque
def solution(arr):
    answer = 0
    s = []
    q = deque(arr)
    while q:
        x = q.popleft()
        s.append(x)
        if s[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                s.pop()
    return answer