from itertools import permutations
def solution(k,d):
    answer = 0
    arr = [i for i in range(len(d))]
    for i in list(permutations(arr,len(d))):
        cnt = 0
        tmp = k
        for step in i:
            if tmp >= d[step][0]:
                tmp -= d[step][1]
                cnt += 1
        answer = max(answer,cnt)
    
    return answer