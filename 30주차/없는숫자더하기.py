def solution(numbers):
    result = 0
    arr = [i for i in range(10)]
    check = [0] * 10
    for i in numbers:
        check[i] = 1
    for i,v in enumerate(check):
        if v == 0:
            result +=i
            
    return result
# 프로그래머스 - 없는 숫자 더하기