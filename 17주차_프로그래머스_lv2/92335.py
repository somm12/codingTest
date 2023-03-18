import math
def makeK(n,k):
    answer = ''
    while n != 0:
        d = n%k
        n = n//k
        answer += str(d)
    return answer[::-1]
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    trans = makeK(n,k)
    s = ''
    for i in range(len(trans)):
        if trans[i] == '0':
            if s != '' and isPrime(int(s)):
                answer +=1
            s = ''
        else:
            s += trans[i]
    if s != '':
        if isPrime(int(s)):
            answer += 1
    return answer
                
# k진수에서 소수 개수 구하기