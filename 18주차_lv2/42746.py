def solution(numbers):
    answer = ''
    arr = []
    for i in numbers:
        arr.append(str(i))
    
    arr.sort(key=lambda x: (x*4)[:4],reverse=True)
    for i in arr:
        answer += i
    if answer[0] == '0':
        answer = '0'
    return answer
# 가장 큰 수 