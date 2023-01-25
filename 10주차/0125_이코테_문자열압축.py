def sol2(s,n):
    li = [s[i : i + n] for i in range(0,len(s), n)]
    res = []
    cnt = 1
    previous = li[0]
    for i in range(1, len(li)):
        if li[i] == previous:
            cnt += 1
        else:
            if cnt != 1:
                res.append(str(cnt))
            res.append(previous)
            previous = li[i]
            cnt = 1
    # 마지막 부분 추가.
    if cnt != 1:
        res.append(str(cnt))
    res.append(previous)
    return len(''.join(res))

def solution(s):
    answer = len(s)
    for i in range(1, len(s) + 1):
        answer = min(answer, sol2(s,i))
    return answer

print(solution('abcabcdede'))