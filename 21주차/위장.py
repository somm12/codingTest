from collections import defaultdict
def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for name, kind in clothes:
        d[kind] += 1
    a = list(d.values())
    for i in a:
        answer *= (i+1)
    
    return answer-1