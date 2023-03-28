def solution(topping):
    answer = 0
    a = {}
    a[topping[0]] = 1
    b = {}
    for i in topping[1:]:
        if not i in b:
            b[i] = 1
        else:
            b[i] += 1
    for i in topping[1:]:
        a[i] = 1
        b[i] -= 1
        if b[i] == 0:
            del(b[i])
        if len(a) == len(b):
            answer+= 1
    return answer
# 롤케이크 자르기