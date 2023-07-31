n,k = map(int,input().split())
cnt = 0
while True:
    target = (n//k)*k# 현재 n보다 작은 수중 가장 가까운 K의 배수.
    cnt += (n-target) # 배수가 될때까지 연산 횟수 더하기.(뺄셈횟수)
    n = target
    if n < k: # n < K가 되는 순간 break.
        break
    n //= k # 배수가 되면 k로 나누기.
    cnt += 1
cnt += (n-1) # 남은 숫자 -1 만큼 더해준다(뺄셈 횟수 더하기)
print(cnt)