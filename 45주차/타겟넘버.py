answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(L,total):
        global answer
        if L == n:
            if total == target:
                answer += 1
            return
        dfs(L+1, total+numbers[L])
        dfs(L+1,total-numbers[L])
    dfs(0,0)
 
   
    return answer
# 프로그래머스 dfs 문제