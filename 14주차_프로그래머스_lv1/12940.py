def solution(n, m):
    answer = []
    maxV = 0
    target = min(n,m)
    for i in range(target,0,-1):
        if n % i == 0 and m % i == 0:
            maxV = i
            break
    answer = [maxV, maxV*(n//maxV)*(m//maxV)]
    return answer
#최대공약수와 최소공배수