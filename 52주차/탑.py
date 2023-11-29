n = int(input())
arr = list(map(int,input().split()))
answer = []
stack = []
for i in range(n):
    if len(stack) == 0:# 맨 앞이기 때문에, 0
        answer.append(0)
        stack.append([arr[i],i])
    else:# 앞쪽에 작은 값이 있으면 pop. -> 왼쪽 방향으로 레이저를 쏘고, 가장 가깝고 큰 값이면 됨. 이전의 더 작은 값은 없앤다.
        while stack and stack[-1][0] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            answer.append(0)
        else:
            answer.append(stack[-1][1]+1)# 해당 인덱스이기 때문에 +1
        stack.append([arr[i],i])

for v in answer:
    print(v,end=' ')
# 백준 자료구조 문제.