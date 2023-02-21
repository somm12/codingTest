def solution(n):
    answer = ''
    s = '수박'
    if n % 2 == 0:
        answer = s*(n//2)
    else:
        answer = s*(n//2) + s[0]
            
    return answer
# 수박수박수박?