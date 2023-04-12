from collections import deque
def solution(cacheSize, cities):
    answer = 0
    c = deque()
    if cacheSize == 0:
        return len(cities)*5
    for i in cities:
        i = i.lower()
        if i in c:
            answer += 1
            c.remove(i)
            c.append(i)
        else:
            answer += 5
            if len(c) < cacheSize:
                c.append(i)
            else:
                c.popleft()
                c.append(i)
    
    return answer
# 캐시 사이즈가 0 인 경우는 항상 5만큼 걸리는 것에 유의