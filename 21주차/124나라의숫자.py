def solution(n):
    answer = []
    while n > 0:
        a = n % 3
        b = n// 3
        if a == 0:
            answer.append('4')
            n = b - 1
        else:
            answer.append(str(a))
            n = b
    answer.reverse()
    return ''.join(answer)