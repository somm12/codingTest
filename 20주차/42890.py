from itertools import combinations
def solution(relation):
    answer = 0
    idxs = [i for i in range(len(relation[0]))]
    avoid = {}
    for i in range(1,len(relation[0])+1):
        for arr in list(combinations(idxs,i)):
            stop = False
            for j in list(avoid.keys()):
                if set(j) < set(arr):
                    stop = True
                    break
            if stop:
                continue
            dict = {}
            for r in range(len(relation)):
                a = []
                for k in arr:
                    a.append(relation[r][k])
                a = tuple(a)
                dict[a] = 1
            if len(dict) == len(relation):
                avoid[arr] = 1
    return len(avoid)

# 후보키
# {} < {} 오른쪽 집합에 포함 여부를 알 수 있음.