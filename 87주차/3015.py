n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
stk =[]
answer = 0
for i in range(n):
    cnt = 1
    while stk and stk[-1][0] <= arr[i]:# 큰값이 오면 더이상 그 전의 값들로 쌍을 만들지 못함. 그리고 같은 값의 개수를 누적합해서 개수를 센다.
        answer += stk[-1][1]
        if stk[-1][0] == arr[i]:
            cnt = stk[-1][1] + 1
        else:# 다른 값이 오면 다시 1개.
            cnt = 1
        stk.pop()
    if stk:answer += 1# 내림 차순인 경우. 자기자신하나씩 계산하는 것과 같음.

    stk.append((arr[i],cnt))
print(answer)
# 백준 오아시스 재결합.
# 여러 경우를 생각해서 도출해야하는 문제.