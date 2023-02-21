def solution(s):
    n = len(s)
    if s.isnumeric() and (n == 4 or n == 6):
        return True
    else:
        return False
        
# 문자열 다루기 기본.