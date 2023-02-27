def solution(a, b, n):
    answer = 0
    while a <= n:
        answer += (n//a)*b
        n = n- ((n//a)*a) + (n//a)*b
        
    return answer
# 콜라문제