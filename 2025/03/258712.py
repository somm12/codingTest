from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    nxtMonth = defaultdict(int)
    nameIdx = {}
    presentNum = defaultdict(int)
    n = len(friends)
    for i,v in enumerate(friends):
        nameIdx[v] = i
    table = [[0]*n for _ in range(n)]

    for v in gifts:
        i,j = v.split(" ")
        a = nameIdx[i]
        b = nameIdx[j]
        table[a][b] += 1
        presentNum[a] += 1
        presentNum[b] -= 1
    
    for i in range(n):
        for j in range(i,n):
            if i == j: continue
            
            v1,v2 = table[i][j], table[j][i]
            if v1 > 0 or v2 > 0:
                if v1 > v2:
                    nxtMonth[i] += 1
                elif v1 < v2:
                    nxtMonth[j] += 1
                else:# 주고 받은 수가 같은 경우
                    if presentNum[i] > presentNum[j]:
                        nxtMonth[i] += 1
                    elif presentNum[i] < presentNum[j]:
                        nxtMonth[j] += 1
            else:# 주고 받은 기록이 없는 경우
                if presentNum[i] > presentNum[j]:
                        nxtMonth[i] += 1
                elif presentNum[i] < presentNum[j]:
                        nxtMonth[j] += 1
    
    ret = list(nxtMonth.values())# 다음달에 받는 선물 값들을 담은 배열.
    
    
    if len(ret) > 0:
        return max(ret)
    return 0# 빈 배열인 경우(아무도 선물을 받지 못하는 경우)
# 프로그래머스 가장 많이 받은 선물