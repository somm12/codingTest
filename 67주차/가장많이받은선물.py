def combi(n):
    ans = []
    def dfs(start,res):
        if len(res) == 2:
            ans.append(res)
            return
        for i in range(start,n):
            dfs(i+1,res+[i])
    dfs(0,[])
    return ans

def solution(friends, gifts):
    name = {}
    n = len(friends)
    arr = [[0]*n for _ in range(n)]
    giftNum = {}# 선물 지수
    get = [0]*n # 최종적으로 받을 선물 개수
    
    for i,v in enumerate(friends):
        name[v] = i
    
    
    for v in gifts:
        a,b = v.split(" ")
        idx1 = name[a]
        idx2 = name[b]
        arr[idx1][idx2] += 1
    
    
    #선물지수 구하기
    for j in range(n):
        total = 0
        for i in range(n):# 받은 것.
            total += arr[i][j]
        giftNum[j] = (sum(arr[j]) - total)
    
    
    
    combination = combi(n)
    
    
    for idx1,idx2 in combination:
        v1 = arr[idx1][idx2]
        v2 = arr[idx2][idx1]
        if (v1 > 0 or v2 > 0) and v1!= v2:# 기록이 있고, 값이 서로 다르면.
            if v1> v2:
                get[idx1] += 1
            else:
                get[idx2] += 1
        else:# 선물지수 비교.
            if giftNum[idx1] > giftNum[idx2]:
                get[idx1] += 1
            elif giftNum[idx2] > giftNum[idx1]:
                get[idx2] += 1
    
    
    return max(get)
                