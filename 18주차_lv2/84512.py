tmp = []
dict =[]
def dfs(L,arr):
    if L == 5:
        return
    for i in arr:
        tmp.append(i)
        dict.append(''.join(tmp))
        dfs(L+1,arr)
        tmp.pop()
def solution(word):
    answer = 0
    dfs(0,['A','E','I','O','U'])
    for i in range(len(dict)):
        if dict[i] == word:
            return i+1
    
    
    return answer
# 모음사전