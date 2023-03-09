def solution(n):
    answer = 0
    s = 0
    e = s+1 
    total = s+e
    while s <= e:
        if total <= n:
            if total == n:
                answer += 1
            e += 1
            total += e
        else:
            total -= s
            s += 1
    return answer
# 숫자의 표현
# 범위는 자연수 부터 10,000 이므로
# s는 0부터 시작해야 n == 1일 경우를 포함.

# 아래는 투 포인터 다른 풀이
def solution(n):
    target = n
    cnt = 0
    total= 0
    e = 1
    for s in range(1,n+1):
        while total < target and e <= n:
            total += e
            e += 1
        if total == target:
            cnt += 1
        total -= s
        
    
    
    return cnt