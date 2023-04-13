from collections import defaultdict
def solution(s):
    answer = []
    s = s[2:-2]
    s = list(s.split("},{"))
    arr = []
    for i in s:
        arr.append(list(map(int,i.split(","))))
    
    arr.sort(key=len)
    dict = defaultdict(int)
    for i in arr:
        for j in i:
            dict[j] = 1
    
    return list(dict.keys())