
answer = 0
def calc(res,tmp):# 우선순위가 담긴 res, 계산할 배열이 담긴 tmp => [100,'-',20,,,]
    stack = []
    arr = tmp[:] # 참조한 배열 값이 변경되지 않도록 복사.
    for op in res: # 우선순위에 따라 계산하기.
        stack = []
        while arr:
            a= arr.pop(0)
            if a == op: # 해당 연산자라면 stack의 맨 뒤, arr의 맨앞 두 숫자끼리 계산하기
                if op == '*':
                    value = stack.pop()*arr.pop(0)
                    stack.append(value)
                elif op == '+':
                    value = stack.pop()+arr.pop(0)
                    stack.append(value)
                elif op == '-':
                    value = stack.pop()-arr.pop(0)
                    stack.append(value)
            else:
                stack.append(a)
        
        arr = stack # 이어서 계산할 수 있도록 arr 업데이트.
 
    return stack[0]# 계산 결과 남은 값 반환.
def comb(res,arr,kind,visited):# 순열을 구하는 함수. 
    global answer
    if len(res) == len(kind):
        answer = max(abs(calc(res,arr)),answer)# 최댓값으로 업데이트.
        return
    for i in range(len(kind)):
        if not visited[i]:
            visited[i] =1
            comb(res+kind[i],arr,kind,visited)
            visited[i] = 0
def solution(expression):
    global answer
    arr = []# exprssion을 계산할 수 있는 형태 배열로 만들기.
    tmp = '' # 숫자를 임시적으로 담을 변수.
    kind = [] # 연산자 종류를 담을 배열.
    for v in expression:
        if not v.isdigit():
            arr.append(int(tmp))
            arr.append(v)
            kind.append(v)
            tmp = ''
        else:
            tmp += v
    arr.append(int(tmp))
    kind = list(set(kind))
    kind = ''.join(kind) # 다시 문자열로 만들기.
    visited = [0]*(len(kind)) # 순열을 구하기 위해서 visited 방문처리 배열 사용.

    comb('',arr,kind,visited)# 우선순위를 만든 후, 계산 수행후, 값 업데이트.
    return answer