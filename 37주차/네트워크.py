def solution(n, computers):
    answer = 0
    g = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i !=j and computers[i][j] == 1:
                g[i+1].append(j+1)

    visited = [0]*(n+1)
    
    def dfs(i):
        visited[i] = 1
        for v in g[i]:
            if not visited[v]:
                dfs(v)
    # def dfs(i):
    #     visited[i]= 1
    #     for j in range(1,n+1):
    #         if computers[i-1][j-1] and not visited[j]:
    #             dfs(j)
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
# 프로그래머스 네트워크