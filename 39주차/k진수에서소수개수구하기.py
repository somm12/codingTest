def isPrime(num):# 소수인지 확인하는 함수.
    if num == 1:# 1은 소수가 아님.
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def solution(n,k):
    answer = 0
    s =''
    while n > 0:
        s += str(n%k)
        n //= k
    s= s[::-1]# k진수로 만든 것 다시 거꾸로.
    arr = s.split('0')# 0을 기준으로 쪼개기.
    for v in arr:
        if len(v) >0:# 빈 문자열도 존재하므로, 유의하기.
            if isPrime(int(v)):
                answer +=1
    return answer
# 프로그래머스 카카오문제.