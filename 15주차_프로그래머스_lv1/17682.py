def solution(dartResult):
    stack = []
    bonus = {'S':1, 'D':2, 'T':3}
    dartResult = dartResult.replace("10","A")
    for i in dartResult:
        if i.isdigit() or i == 'A':
            stack.append(10 if i == 'A' else int(i))
        elif i in ("S","D","T"):
            n = stack.pop()
            stack.append(n ** bonus[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == "*":
            if len(stack):
                n = stack.pop()
                if len(stack):
                    stack[-1] *= 2
                stack.append(n*2)
    
    return sum(stack)
# 카카오 다트게임. 
# 딕셔너리, stack의 pop 사용으로 최근 값과 계산하기 수월.
# 10 제외 모든 점수가 한 자리 수이기 때문에 replace 사용하여 미리 대비.