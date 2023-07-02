def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer
# 프로그래머스 문제.