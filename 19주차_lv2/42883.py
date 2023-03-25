def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    for i,v in enumerate(number):
        while stack and stack[-1] < v:
            stack.pop()
            cnt += 1
            if k == cnt:
                return ''.join(stack) + number[i:]
        stack.append(v)
    
    return ''.join(stack[:len(stack)-k])
# 큰 수 만들기