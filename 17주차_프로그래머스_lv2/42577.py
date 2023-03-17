def solution(phone_book):
    answer = True
    dict = {}
    phone_book.sort(key=len)
    for i in phone_book:
        if len(dict) == 0:
            dict[i] = 1
        else:
            tmp = ''
            for s in i:
                tmp += s
                if tmp in dict:
                    return False
            dict[i] = 1
    return answer
# 전화번호 목록