n,m,k=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
cnt = 1
answer =0
for _ in range(m):
    if cnt > k:
        answer += arr[1]
        cnt = 1
    else:
        answer += arr[0]
    cnt += 1
print(answer)

# 더 빠른 코드
# 큰 수 k번, 두번째로 큰수 1번 더해지는 규칙 => (m//k+1) * k + m%(k+1): 큰 수가 더해지는 횟수.
# m- (큰수가 더해진 횟수) : 두번째로 큰수가 더해지는 횟수.

first= arr[0]
second = arr[1]

firstCount = (m//(k+1))*k # 괄호 조심.

firstCount += m%(k+1) # 주의 나누어 떨어지지 않을 경우.
secondCount = m - firstCount

result = firstCount*first + secondCount*second
print(result)
