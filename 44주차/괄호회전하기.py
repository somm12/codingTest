from collections import deque
def check(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        else:
            tmp = stack[-1]
            if tmp == '(' and x == ')':
                stack.pop()
            elif tmp == '[' and x == ']':
                stack.pop()
            elif tmp == '{' and x == '}':
                stack.pop()
            else:
                stack.append(x)
    return len(stack) ==0
def solution(s):
    answer =0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate(-1)
        if check(s):
            answer += 1
        
    
    return answer
    # 프로그래머스 - 괄호 회전하기
    # 문자열 문제 연습.