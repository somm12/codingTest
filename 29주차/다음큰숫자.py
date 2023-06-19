def solution(n):
    answer = 0
    tmp = n+1
    cnt = bin(n).count('1')
    while True:
        num = bin(tmp).count('1')
        if cnt == num:
            answer =tmp
            break
        tmp += 1
    return answer

# 프로그래머스 lv2