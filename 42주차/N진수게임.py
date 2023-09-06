def convert(num,n):# n진수로 변환하기.
    arr = '0123456789ABCDEF' # 변환시 10~ 15는 A ~ F로 표현.
    result = []
    if num == 0:
        return '0'
    while num > 0:
        a = num%n
        result.append(arr[a])
        num //= n
    result = result[::-1]
    return ''.join(result)
def solution(n,t,m,p):
    answer = ''
    for i in range(0,t*m+1):
        res = convert(i,n)
        answer += res
        if len(answer) >= t*m:# 이미 t*m개수 이상이 된다면 break.
            break
    return ''.join(answer[p-1:t*m:m])# p번째부터 t*m개수 만큼, m마다 p의 순서가 돌아오므로 인덱싱 이용.
# 프로그래머스 카카오 문제