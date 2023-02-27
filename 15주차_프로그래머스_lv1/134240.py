from collections import deque
def solution(food):
    answer = ''
    l = []
    r = deque([])
    for i in range(1,len(food)):
        for _ in range(food[i]//2):
            l.append(str(i))
            r.appendleft(str(i))
    answer = ''.join(l) + '0' + ''.join(r)
    return answer

#푸드 파이터 대회.