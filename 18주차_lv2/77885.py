def countOne(x):
    x = bin(x)[2:]
    tmp = 0
    cnt = 1
    for i in x[::-1]:
        if i == '1':
            tmp += 1
            cnt = max(cnt,tmp)
            
        else:
            break
    return cnt
    
def solution(numbers):
    answer = []
    for i in numbers:
        t = countOne(i)
        answer.append(2**(t-1)+i)
    return answer
# 2개 이하로 다른 비트