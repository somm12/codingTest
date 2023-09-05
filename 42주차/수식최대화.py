answer =0
def calc(res,arr):# ['*','-','+'] 순서대로 계산 수행. 
    q = arr[:]# 원본 배열을 해치지 않기 위한 복사.
    for op in res:
        stack =[]
        while q:
            v =q.pop(0)
            if v == op:# 현재 우선순위인 연산자를 만나면 계산.
                a=stack.pop()
                b = q.pop(0)
                if op == '*':
                    stack.append(a*b)
                elif op == '+':
                    stack.append(a+b)
                elif op == '-':
                    stack.append(a-b)
            else:
                stack.append(v)
        q = stack[:]
        if len(q) == 1:# 1개가 남는다면 return
            return q[0]
                
def solution(expression):
    
    tmp = ''
    arr = []
    op = []
    for i,v in enumerate(expression):
        if v.isdigit():
            tmp += v
        else:
            op.append(v)
            arr.append(int(tmp))
            tmp = ''
            arr.append(v)
    arr.append(int(tmp)) # 숫자와 연산자 분리.
    op = list(set(op))
    n = len(op)
    visited = [0]*n
    
    def dfs(res):
        global answer
        if len(res) == n:
            answer = max(answer,abs(calc(res,arr)))
            return
        for i,v in enumerate(op):
            if not visited[i]:
                visited[i] =1
                dfs(res+v)
                visited[i] = 0
    dfs('')
    
    return answer
# 카카오 문제 복습.