answer = 0
def dfs(L,op,n,arr,target):
    global answer
    if L == n:
        total = 0
        for i in range(len(op)):
            if op[i] == '+':
                total += arr[i]
            else:
                total -= arr[i]
        if total == target:
            answer += 1
    else:
        for i in ['+','-']:
            op.append(i)
            dfs(L+1,op,n,arr,target)
            op.pop()
    return answer

    
def solution(numbers, target):
    return dfs(0,[],len(numbers),numbers,target)
# 타겟 넘버

# 아래는 for문을 사용하지 않고 작성한 코드.

answer = 0
def dfs(idx,numbers,target,total):
    global answer
    n = len(numbers)
    if idx == n and total == target:
        answer += 1
        return
    if idx == n:
        return
    dfs(idx+1,numbers,target,total+numbers[idx])
    dfs(idx+1,numbers,target,total-numbers[idx])

def solution(numbers, target):
    dfs(0,numbers,target,0)
    return answer