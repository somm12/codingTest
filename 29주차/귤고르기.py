from collections import defaultdict
def solution(k, tangerine):
    result = 0
    dict = defaultdict(int)
    for v in tangerine:
        dict[v] += 1
    
    arr = list(dict.values())
    arr.sort(reverse=True)
    kind = 0
    total = 0
    for v in arr:
        kind += 1
        total += v
        if total >= k:
            break
    return kind

# 프로그래머스 lv2