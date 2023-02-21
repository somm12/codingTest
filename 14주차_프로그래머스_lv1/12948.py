def solution(s):
    n = len(s)
    idx = n - 4
    answer = '*'*idx + s[-4:]
    return answer