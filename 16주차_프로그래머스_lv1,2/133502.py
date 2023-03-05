def solution(ingredient):
    stack = []
    ans = 0
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if stack[-1] == 1:
                if stack[-4:] == [1,2,3,1]:
                    ans += 1
                    for _ in range(4):
                        stack.pop()
    return ans
# 햄버거 만들기