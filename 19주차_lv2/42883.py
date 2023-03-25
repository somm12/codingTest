def solution(number, k):
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
# ** 항상 반복문 내 return 은 예외 경우에 대비하여 가장 바깥 부분에 return도 생각하자.