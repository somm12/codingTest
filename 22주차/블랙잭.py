


def dfs(L,start):
    global ans
    if L==3:
        tmp = sum(res)
        if tmp <= m:
            ans = max(ans,tmp)
        return
    
    for i in range(start,len(arr)):
        res.append(arr[i])
        dfs(L+1,i+1)
        res.pop()
    
ans = -1
res = []
n,m = map(int,input().split())
arr = list(map(int,input().split()))
dfs(0,0)
print(ans)