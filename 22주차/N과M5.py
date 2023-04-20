def dfs(L):
    if L == m:
        for i in res:
            print(i,end = ' ')
        print()
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            res.append(arr[i])
            dfs(L+1)
            visited[i] = 0
            res.pop()
n,m = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort()
visited = [0]*n
res = []
dfs(0)