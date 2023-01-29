def check(s):
    a = []
    for i in range(len(s)):
        if len(a) != 0:
            if a[-1] == '(' and s[i] == ')':
                a.pop()
            else:
                a.append(s[i])
        else:
            a.append(s[i])
    if len(a) > 0:
        return False
    else:
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
            u = s[:i+1]
            v = s[i+1:]
            return [u,v]
def sol(p):
    ans = ''
    temp = ''
    if len(p) == 0:
        return ans
    if check(p):
        return p
    u,v = divide(p)
    while check(u):
        ans += u
        u, v = divide(v)
    temp = '(' + v + ')'
    u = u[1:len(u)-1]
    t = ''
    for i in u:
        if i == '(':
            t += ')'
        else:
            t += '('
    ans += temp + t
    return ans

print(sol("(()())()"))