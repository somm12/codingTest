def solution(phone_book):
    answer = True
    dict = {}
    for v in phone_book:
        dict[v] = 1
    for v in phone_book:
        tmp = ''
        for s in v:
            tmp += s
            if tmp in dict and v != tmp:# 접두사가 번호로 존재한다면 체크. 단, 문자열이 일치하면 접두사가 아님에 조심.
                return False
    return answer 