def solution(s):
    answer = ''
    arr = s.split(" ")
    for i in arr:
        for j in range(len(i)):
            if i[0].isdigit():
                answer += i[j].lower()
            else:
                if j == 0:
                    answer += i[j].upper()
                else: answer += i[j].lower()
        answer += ' '
    return answer[:-1]
# JadenCase 문자열 만들기.
# 공백이 연속이 가능하다는 것이 포인트