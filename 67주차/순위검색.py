# 배열은 딕셔너리에 키로 못씀.
from bisect import bisect_left
def solution(info,query):
    answer = []
    arr = [['cpp','java','python','-'], ['backend','frontend','-'],['junior','senior','-'],['chicken','pizza','-']]
    dict = {}
    def dfs(L,res):
        if L > 4:
            return
        if len(res) == 4:
            dict[tuple(res)] = []
            return
        for i in range(len(arr[L])):
            dfs(L+1, res + [arr[L][i]])
    dfs(0,[])
    
    def dfs2(qu,score):
        def d(L,res):
            if L > 4:
                return
            if len(res) == 4:
                
                dict[tuple(res)].append(score)
                return 
            for i in range(len(qu[L])):
                d(L+1, res+ [qu[L][i]])
        d(0,[])
    
    for v in info:# 조심
        tmp = v.split(" ")
        score = int(tmp[-1])
        tmp = tmp[:-1]
        qu = []
        for condition in tmp:# 조건에 해당하는 부분만이 아닌 조건이 빠진 경우도 점수가 포함된다!! python - - - , python backend - - 이 모든 경우에 다 포함.
            qu.append([condition] + ['-'])
        
        dfs2(qu,score)
    
    for key in dict:
        dict[key].sort()
    
    for v in query:
        key = v.split(" and ")
        
        condi,score = key[-1].split(" ")# 마지막 점수부분은 공백으로 나눠야함.
        key = key[:3] + [condi]
        
        key = tuple(key)
        
        answer.append(len(dict[key]) - bisect_left(dict[key], int(score)))
    return answer