from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    for i in tangerine:
        dict[i] += 1
    arr = list(dict.values())
    arr.sort(reverse=True)
    total = 0
    for i,v in enumerate(arr):
        total += v
        if total>=k:
            return i+1
    return answer 