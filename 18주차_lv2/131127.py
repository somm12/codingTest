import copy
def solution(want, number, discount):
    answer = 0
    dict = {}
    n = len(want)
    for i in range(n):
        dict[want[i]]= number[i]
    cnt = 0
    tmp = dict.copy()
    
    for i in range(len(discount)-9):
        for j in range(i,i+10):
            v = discount[j]
            if v in dict:
                tmp[v] -= 1
                if tmp[v] == 0:
                    cnt += 1
                if cnt == n:
                    answer += 1
        tmp = dict.copy()
        cnt = 0

    
    return answer
# 할인 행사