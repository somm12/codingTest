def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])[2:]
        a = a.rjust(n,'0')
        a = a.replace('0',' ')
        a = a.replace('1','#')
        answer.append(a)
    return answer
# 비밀지도 - 카카오 2018

# 알게된 것
# 비트 연산자  &, |, ^, ~ => 차례로 AND, OR, XOR, NOT
# str.ljust(숫자) => 오른쪽 끝에 공백을 채워줌
# str.rjust(숫자) => 왼쪽 끝에 공백을 채워줌