n = int(input())
arr = list(map(int,input().split()))
answer = -1001
total = 0
for v in arr:
    total += v
    answer = max(answer,total)
    if total < 0:
        total = 0
print(answer)
# 백준 연속 합 문제
# 음수를 더한다고 해서 항상 손해는 아니기에 더해보고, 음수가 나오면 0으로 다시 시작.