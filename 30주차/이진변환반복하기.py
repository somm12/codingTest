def solution(s):
    result = ''
    cnt = 0
    zero = 0
    while s != '1':
        cnt += 1
        temp = 0
        for i in s:
            if i == '1':
                temp += 1
            else:
                zero += 1
        s = bin(temp)[2:]
    return [cnt, zero]
# 프로그래머스