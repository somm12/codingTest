
def dfs(L, res,total,now):
    global ans
    # 경로 비용이 이미 현재까지의 최솟값보다 많아 졌다면 return
    if total > ans:
        return
    if L == n:
        # 마지막 지점에서 출발지점으로 가는 경로가 존재할 경우.
        if w[res[n-1]][res[0]] != 0:
            total += w[res[n-1]][res[0]]
            ans= min(ans,total)
        return
    
    for i in range(n):
        # 다음 지점 경로가 존재하는지 확인 필수.
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