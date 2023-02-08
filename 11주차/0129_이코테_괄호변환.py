def check(w):
    cnt = 0
    for i in w:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True
def divide(w):
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return [w[:i+1],w[i+1:]]
def solution(p):
    answer = ''
    if p == '':
        return ''
    u,v = divide(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v) + ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer
