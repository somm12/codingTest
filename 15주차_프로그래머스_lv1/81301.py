def solution(s):
    answer = 0
    t = ['zero','one','two','three','four','five','six','seven','eight','nine']
    if s.isdecimal():
        return int(s)
    for i in range(10):
        if t[i] in s:
            s = s.replace(t[i], str(i))
    answer = int(s)
    return answer
# 숫자 문자열과 영단어
# replace는 문자열을 반환하므로, 바뀐 값을 넣어주어야함.