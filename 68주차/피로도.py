answer = 0
def solution(k,dungeons):
    n = len(dungeons)
    visited = [0]*n
    def dfs(L,remain):
        global answer
        if L > n:
            return
        answer = max(answer,L)
        for i in range(n):
            if not visited[i] and remain >= dungeons[i][0]:# 최소 필요 피로도 체크.
                visited[i] = 1
                dfs(L+1, remain-dungeons[i][1])# 소모 피로도 반영
                visited[i] = 0
    dfs(0,k)
    return answer