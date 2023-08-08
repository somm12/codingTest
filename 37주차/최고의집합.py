def solution(n, s):
    answer = []
    while n > 0:
        if s//n == 0:
            return [-1]
        tmp = s//n
        s = s-tmp
        n -=1
        answer.append(tmp)
    return answer
# 프로그래머스 최고의 집합