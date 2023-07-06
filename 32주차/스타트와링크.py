n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
visited = [0]*n
answer = int(1e9)

def dfs(L,start): # visited 를 이용해서 팀 조합을 구하고, 1, 0인 값이 나누어져서 각 팀의 능력치를 구할 수 있음.
    global answer, visited
    if L==n//2:
        s = 0
        l = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    s += g[i][j]
                elif not visited[i] and not visited[j]:
                    l += g[i][j]
        answer = min(answer, abs(s-l))
        return
    for i in range(start,n):
        visited[i] = True
        dfs(L+1,i+1)
        visited[i] = False
dfs(0,0)
print(answer)