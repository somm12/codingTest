def solution(s):
    answer = True
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    if cnt != 0:
        answer = False
    return answer
# 올바른 괄호.
# 아래는 스택을 이용한 풀이
def solution(s):
    stack = []
    for i in s:
        if stack:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
        else:
            if i == ')':
                return False
            else:
                stack.append(i)
            
    return len(stack) == 0
