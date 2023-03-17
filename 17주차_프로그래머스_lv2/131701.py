def solution(elements):
    answer = []
    res = set()
    n = len(elements)
    for i in range(n-1):
        elements.append(elements[i])
    for s in range(n):
        total = 0
        for k in range(s, s+n):
            total += elements[k]
            res.add(total)
    
    return len(res)
# 연속 부분 수열 합의 개수