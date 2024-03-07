def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        v = arr1[i] | arr2[i]
        s = bin(v)[2:]
        s = s.rjust(n,'0')
        tmp = s.replace('0',' ')
        tmp = tmp.replace('1', '#')
        answer.append(tmp)
    return answer