def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer += 1
    answer *= 2
    if n **0.5 == int(n**0.5):
        answer -= 1
    return answer
# 프로그래머스 문제 