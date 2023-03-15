import math
def solution(progresses, speeds):
    answer = []
    s = []
    for i in range(len(progresses)):
        s.append(math.ceil((100-progresses[i])/speeds[i]))
    cnt = 0
    now = s[0]
    
    for i in s:
        if now < i:
            answer.append(cnt)
            now = i
            cnt = 0
        cnt += 1
    answer.append(cnt)
    
    return answer
# 기능 개발