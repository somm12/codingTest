def isPrime(num):# 소수 판별.
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = list(numbers)
    n = len(arr)
    visited = [0]*n
    res = []
    def dfs(tmp):
        
        if 1 <= len(tmp) <= n:# 모든 카드를 사용해서 나올 수 있는 수 구하기.
            res.append(int(tmp))
        
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(tmp+arr[i])
                visited[i] = 0
    dfs('')
    res = list(set(res))# 중복 제거.
    
    for v in res:
        if isPrime(v):
            answer += 1
    return answer
