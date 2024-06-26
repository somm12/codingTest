n = int(input())
arr = list(map(int,input().split()))
stk = [0]

answer = [-1]*n# 오큰수 없으면 -1
for i in range(1,n):
    while stk and arr[i] > arr[stk[-1]]: # 스택의 가장 마지막 수가, 오른쪽에 있는 수보다 작은 순간 pop하고 짝을 짓듯 오큰수 찾기.
        idx = stk.pop()
        answer[idx] = arr[i]
    stk.append(i)


for v in answer:
    print(v,end=' ')
# 백준 오큰수.