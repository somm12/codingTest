from itertools import combinations
def solution(relation):
    answer = []
    li = [i for i in range(len(relation[0]))]
    for cnt in range(1, len(relation[0])+1):
        for arr in list(combinations(li,cnt)):
            dict = {}
            flag = False
            for i in answer:
                if set(i) < set(arr):
                    flag = True
                    break
            if flag:
                continue
            for i in range(len(relation)):
                tmp = []
                for j in arr:
                    tmp.append(relation[i][j])
                dict[tuple(tmp)] = 1
            
            if len(dict) == len(relation):
                answer.append(arr)
    print(answer)
    return len(answer)
    