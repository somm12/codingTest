def dfs(L):
    if L == m:
        for i in res:
            print(i,end =' ')
        print()
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            res.append(i)
            dfs(L+1)
            visited[i] = 0
            res.pop()
n, m =map(int,input().split())
res = []
visited = [0]*(n+1)
dfs(0)