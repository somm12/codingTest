def solution(s):
    answer = True
    n = len(s)
    for i in s:
        if not i.isnumeric():
            return False
    if n == 4 or n == 6:
        return True
    else:
        return False
        
# 문자열 다루기 기본.