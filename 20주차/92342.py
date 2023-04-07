def score(a,b):
    s1 = 0
    s2 = 0
    for i in range(11):
        if a[i] > b[i]:
            s1 += (10- i)
        
        elif a[i] < b[i]:
            s2 += (10 -i)
        
        elif a[i] == b[i] and a[i] !=0:
            s2 += (10 -i)
    return s1-s2
def solution(n, info):
    answer = []
    arr = {}
    res = [0] * 11
    def dfs(L,total):
        if L == 11 or total >= n:
            a = score(res,info)
            if a > 0:
                arr[tuple(res)] = a
            return
        res[L] = info[L] + 1
        if total + res[L] <= n:
            dfs(L+1, total+res[L])
        res[L] = 0
        dfs(L+1,total)
    
    
    dfs(0,0)
    if len(arr) == 0:
        return [-1]
    tmp = max(list(arr.values()))
    for i in list(arr.keys()):
        if arr[i] == tmp:
            answer.append(i)
    answer.sort(key=lambda x: (-x[10],-x[9],-x[8],-x[7],-x[6],-x[5],-x[4],-x[3],-x[2],-x[1],-x[0]))
    answer = list(answer[0])
    if sum(answer) < n:
        answer[-1] = n - sum(answer)
    return answer
   
   
# 양궁대회