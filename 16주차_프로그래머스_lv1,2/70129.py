def solution(s):
    answer = []
    total = 0
    cnt = 0
    while s != '1':
        
        num = s.count('1')
        cnt += len(s) - num
        total += 1
        
        
        s = bin(num)[2:]
    answer = [total, cnt]
    return answer
# 이진 변환 반복하기