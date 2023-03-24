import math
dict = {}

def isPrime(arr):
    n = int(''.join(arr))
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

def dfs(L,res,ch,numbers):
    global dict
    if L == len(numbers):
        return
    for i in range(len(numbers)):
        if ch[i] == 0:
            ch[i] = 1
            res.append(numbers[i])
            if isPrime(res):
                dict[int(''.join(res))] = 1
            dfs(L+1,res,ch,numbers)
            res.pop()
            ch[i] = 0
    
def solution(numbers):
    ch = [0]*(len(numbers))
    res = []
    
    dfs(0,res,ch,numbers)
    return len(dict)
# 소수찾기