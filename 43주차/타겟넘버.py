answer = 0
def solution(numbers, target):
    
 
    def dfs(L,total):
        global answer
        if L == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(L+1, total - numbers[L])
        dfs(L+1, total + numbers[L])
    
    dfs(0,0)
    return answer
# 프로그래머스 고득점 kit. bfs/dfs