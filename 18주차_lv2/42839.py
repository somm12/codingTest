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
# 아래는 permutations 이용한 풀이. 중복과 0이 첫번째 자리에 올 경우 생기는 중복에 조심**
dict = {}
from itertools import permutations
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

    
def solution(numbers):
    a = set()
    for i in range(1,len(numbers)+1):
        for i in list(permutations(list(numbers),i)):
            i = int(''.join(i))
            if isPrime(i):
                a.add(i)
    
    return len(a)