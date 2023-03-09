def solution(s):
    answer = 0
    
    stack = []
    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack) == 0:
        answer = 1


    return answer
# 짝지어 제거하기