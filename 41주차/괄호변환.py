def check(p):# 올바른 괄호인지 확인하는 함수.
    cnt = 0
    for v in p:
        if v == ')':
            cnt -= 1
            if cnt < 0:
                return False
        else:
            cnt += 1
    if cnt == 0:
        return True
    return False

def solution(p):

    if check(p):
        return p
    def go(w):
        if w == '':
            return w
        a,b =0,0
        for i,v in enumerate(w): # u,v로 분리 (u는 더이상 분리할 수 없는 균형잡힌 문자열로.)
            if v == '(':
                a += 1
            else:
                b += 1
            if a == b:
                u = w[:i+1]
                v = w[i+1:]
                break
        if check(u):
            return u+go(v)
        result = '(' + go(v) + ')'
        u = u[1:-1]
        reversedU = ''
        for i in u:# u 반대로 만들기
            if i == '(':
                reversedU += ')'
            else:
                reversedU += '('
        result += reversedU
        return result
    
    return go(p)
# 주어진 설명 그대로 구현.

# 프로그래머스 문제