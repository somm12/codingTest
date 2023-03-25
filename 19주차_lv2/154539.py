def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i, v in enumerate(numbers):
        if not stack:
            stack.append((i,v))
        else:
            while stack and stack[-1][1] < v:
                idx,x = stack.pop()
                answer[idx] = v
            stack.append((i,v))
  
    return answer
# 뒤에 있는 큰 수 찾기