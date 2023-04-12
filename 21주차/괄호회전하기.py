from collections import deque
def check(s):
    stack = []
    for i in s:
        if i in ['(','{','[']:
            stack.append(i)
        else:
            if stack and i == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and i == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        return True
    return False

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.rotate(-1)
        
    return answer