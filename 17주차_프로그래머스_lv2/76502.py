from collections import deque
def check(arr):
    stack = []
    for i in arr:
        if stack:
            x = stack[-1]
            if x == '(' and i == ')':
                stack.pop()
            elif x == '{' and i == '}':
                stack.pop()
            elif x == '[' and i == ']':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return False
    return True
def solution(s):
    answer = 0
    length = len(s)
    q= deque(list(s))
    for i in range(length):
        if i > 0:
            x = q.popleft()
            q.append(x)
        if check(q):
            answer += 1
    return answer
# 괄호 회전하기 - 스택 큐 이용