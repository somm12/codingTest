

def dfs(L,total,res):
    global count
    if L >= n:
        if total == s and len(res)>0:
            count += 1
        return
    dfs(L+1,total+arr[L],res+[arr[L]])
    dfs(L+1,total,res)
n,s = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
count = 0
dfs(0,0,[])
print(count)
