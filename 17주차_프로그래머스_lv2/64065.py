def solution(s):
    answer = []
    s1 = s[2:-2].split('},{')
    ss = []
    for i in s1:
        arr = []
        for v in i.split(","):
            arr.append(int(v))
        ss.append((len(arr),arr))
    ss.sort(key=lambda x: x[0])
    
    for i in ss:
        for value in i[1]:
            if value not in answer:
                answer.append(value)
    return answer
# 튜플
