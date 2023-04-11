def solution(cap, n, d, p):
    answer = 0
    while d:
        if d[-1] == 0:
            d.pop()
        else:
            break
    while p:
        if p[-1] == 0:
            p.pop()
        else:
            break
    while d or p:
        tmp = max(len(d),len(p))
        answer += (tmp*2)
        res = cap
        while d:
            x = d.pop()
            if x <= res:
                res -= x
            else:
                x -= res
                d.append(x)
                break
        pes = cap
        while p:
            v = p.pop()
            if v <= pes:
                pes -= v
            else:
                v -= pes
                p.append(v)
                break
    return answer
# 택배 배달과 수거하기