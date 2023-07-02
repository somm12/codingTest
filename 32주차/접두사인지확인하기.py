def solution(my_string, is_prefix):
    answer = 0
    dict = {}
    a = ''
    for i in my_string:
        a += i
        dict[a] = 1
    if is_prefix in dict:
        answer = 1
    return answer
# 프로그래머스 문제.