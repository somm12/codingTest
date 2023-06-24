def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])[2:]
        a = a.rjust(n,'0')
        a = a.replace('0',' ')
        a = a.replace('1','#')
        answer.append(a)
    return answer
# 프로그래머스