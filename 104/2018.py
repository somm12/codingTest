n = int(input())

end = 0
total = 0
answer = 0
for start in range(1,n+1):
    while end <= n and total < n:
        end += 1
        total += end
    if total == n:
        answer += 1
    total -= start# n보다 큰 경우이기 때문에 start를 빼준다.
        
print(answer)
# 백준 수들의 합 5