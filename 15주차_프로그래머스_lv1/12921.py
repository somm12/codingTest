import math
def solution(n):
    answer = 0
    arr = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
    for i in range(2,len(arr)):
        if arr[i]:
            answer += 1
    return answer
# 소수찾기(에라토스테네스체)