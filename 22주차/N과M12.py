def dfs(L,start):
    if L == m:
        for i in res:
            print(i,end = ' ')
        print()
        return
    for i in range(start,len(arr)):
        res.append(arr[i])
        dfs(L+1,i)
        res.pop()
n,m = map(int,input().split())
arr= list(map(int,input().split()))
arr = list(set(arr))
arr.sort()
res = []
dfs(0,0)