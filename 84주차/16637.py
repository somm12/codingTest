from collections import deque

n = int(input())
num= n//2

arr =list(input())
answer = -int(1e9)
check = [0]*n
s = set(['+','-','*'])
def calc(a,op,b):# 계산.
    a,b = int(a),int(b)
    if op == '+':
        return str(a+ b)
    elif op == '-':
        return str(a-b)
    return str(a*b)

def go(tmp):
    stk = []
    q = deque(arr)
    i = 0
    while q:# 괄호 부분 먼저 연산.
        v = q.popleft()
        if v not in s:
            stk.append(v)
        else:
            if tmp[i] == 1:
                a = stk.pop()
                b = q.popleft()
                stk.append(calc(a,v,b))
                i += 1
            else:
                stk.append(v)
        i += 1
    q= deque(stk)
    stk = []
    while q:# 괄호 먼저 연산 이후, 연산 나머지 처리.
        v = q.popleft()
        if v not in s:
            stk.append(v)
        else:
            
            a = stk.pop()
            b = q.popleft()
            stk.append(calc(a,v,b))
    return int(stk[0])



def dfs(idx,res):# 각 연산자를 기준으로 괄호를 쓸지 말지 여부로 완전탐색을 통해 구하기.
    global answer
    if idx == n:
        answer = max(answer,go(res))
        return
    if idx == 1:
        res[idx] = 1
        dfs(idx+2,res)
        res[idx] = 0
        dfs(idx+2,res)
    else:
        if res[idx-2] == 1:
            dfs(idx+2,res)
        else:
            res[idx] = 1
            dfs(idx+2,res)
            res[idx] = 0
            dfs(idx+2,res)

dfs(1,check)

print(answer)
# 백준 괄호 추가하기.

