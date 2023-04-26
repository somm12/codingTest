
def dfs(L, res,total,now):
    global ans
    if total > ans:
        return
    if L == n:
        if w[res[n-1]][res[0]] != 0:
            total += w[res[n-1]][res[0]]
            ans= min(ans,total)
        return
    
    for i in range(n):
        if L == 0 or (not visited[i] and w[res[L-1]][i] != 0):
            visited[i] = 1
            dfs(L+1,res+[i],total+w[now][i],i)
            visited[i] = 0

ans = int(1e9)
n = int(input())

w = []
for _ in range(n):
    w.append((list(map(int,input().split()))))
visited = [0]*n
dfs(0,[],0,0)

print(ans)