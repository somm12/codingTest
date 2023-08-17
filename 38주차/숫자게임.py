import heapq
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    n = len(A)
    a,b = 0,0
    while a < n and b < n:
        if A[a] < B[b]:
            answer +=1
            a+=1
            b+=1

        else:
            b += 1
            
    return answer
# 프로그래머스 lv3문제