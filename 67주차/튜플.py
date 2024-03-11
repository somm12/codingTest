def solution(s):
    answer =[]
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = lambda x: len(x))
    tmp = []
    check = set()
    for arr in s:
        tmp.append(list(map(int,arr.split(","))))
    for arr in tmp:
        for v in arr:
            if v not in check:
                check.add(v)
                answer.append(v)
            
    return answer