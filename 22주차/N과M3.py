def dfs(L):
    if L == m:
        for i in res:
            print(i,end =' ')
        print()
        return
    for i in range(1,n+1):
        res.append(i)
        dfs(L+1)
        res.pop()
n, m =map(int,input().split())
res = []
dfs(0)