def check(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True
def divide(s):
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
        else:
            b += 1
        if a == b:
            return i

def solution(p):
    answer = ''
    if p == '':
        return p
    if check(p):
        return p
    idx = divide(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if check(u):
        answer += u + solution(v)
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

print(solution("()))((()"))