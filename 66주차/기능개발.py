import math
def solution(progresses,speeds):
    answer = []
    n = len(speeds)
    arr = []
    stack = []
    for i in range(n):
        v = (100- progresses[i])/speeds[i]
        arr.append(math.ceil(v))
    cnt = 1
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
        else:
            if stack[-1] >= arr[i]:# 앞의 기능보다 같거나 적게 걸리면 함께 배포되므로 cnt+1
                cnt += 1
            else:# 더 걸린다면, pop해서 answer에 개수 push
                stack.pop()
                stack.append(arr[i])
                answer.append(cnt)
                cnt = 1
    answer.append(cnt)
    return answer