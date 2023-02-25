cnt = 0
res = []
def dfs(L,s,number):
    global cnt
    if L == 3:
        if sum(res) == 0:
            cnt += 1
        return
    for i in range(s,len(number)):
        res.append(number[i])
        dfs(L+1,i+1,number)
        res.pop()
def solution(number):
    dfs(0,0,number)
    return cnt
# 삼총사