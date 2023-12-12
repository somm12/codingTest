n,k = map(int,input().split())
arr = list(map(int,input().split()))

answer =-1
def dfs(res):
    global answer
    if len(res) > 0 and int(res) > n: return
    if len(res) > 0 and int(res) <= n:
        answer = max(answer,int(res))
    
    for v in arr:
        dfs(res+str(v))

dfs('')
print(answer)