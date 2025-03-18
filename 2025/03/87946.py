answer = 0
def solution(k, dungeons):
    n = len(dungeons)
    visited = [0]*n
    def dfs(now,L):
        global answer
        answer = max(answer,L)
        for i in range(n):
            if not visited[i] and now >= dungeons[i][0]:
                visited[i] = 1
                dfs(now - dungeons[i][1], L+1)
                visited[i] = 0
    dfs(k,0)
    return answer
# 프로그래머스 피로도 