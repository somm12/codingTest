def dfs(L,total,res):
    global cnt
    if total > n:
        return
    if L == 4:
        if total == n:
            tmp = 0
            for i,v in enumerate(res):
                if i == 0:
                    tmp += 1*v
                elif i == 1:
                    tmp += 5*v
                elif i==2:
                    tmp += 10*v
                else:
                    tmp += 50*v
            cnt[tmp] = 1
        return
    
    for i in range(n+1):
        dfs(L+1,total+i,res+[i])

n = int(input())
cnt = {}
dfs(0,0,[])
print(len(cnt))