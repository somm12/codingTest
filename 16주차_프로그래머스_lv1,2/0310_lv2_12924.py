def solution(n):
    answer = 0
    s = 0
    e = s+1 
    total = s+e
    while s <= e:
        if total <= n:
            if total == n:
                print(s,e)
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