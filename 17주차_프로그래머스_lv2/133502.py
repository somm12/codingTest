def solution(arr):
    stack = []
    cnt = 0
    for i in range(len(arr)):
        stack.append(arr[i])
        if len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                cnt += 1
                for _ in range(4):
                    stack.pop()
                    
    return cnt
# 햄버거 만들기 - 복습