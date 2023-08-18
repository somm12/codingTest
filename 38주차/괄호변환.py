def check(s):
    cnt = 0
    i = 0
    while i <len(s):
        if s[i] == ')':
            cnt -= 1
            if cnt < 0:
                return False
        else:
            cnt += 1
        i += 1
    if cnt == 0:
        return True
    return False
def divide(s):
    if s == '':
        return s
    if check(s):
        return s
    l = 0
    r = 0
    i = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            u = s[:i+1]
            v = s[i+1:]
            break
    
    
    if check(u):
        u += divide(v)
        
    else:
        result = '('+ divide(v) + ')'
        u = u[1:len(u)-1]
        tmp = ''
        for i in range(len(u)):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('
        
        result += tmp
        return result
    return u

def solution(p):
    answer = ''
    answer = divide(p)
    return answer
# 프로그래머스 문제