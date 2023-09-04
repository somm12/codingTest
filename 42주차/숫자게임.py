def solution(A,B):
    answer =0
    A.sort() # 오름 차순 정렬. 순서가 정해져도, 이길 수 있는 경우를 구하는 것이기에, 정렬해도 ok.
    B.sort()
    a = 0# A,B 각각의 인덱스
    b = 0 
    while b < len(B):# 작은 인덱스 부터 차례로 A보다 B가 더 큰 숫자가 나올 수 있도록 만든다.
        if A[a] < B[b]:# 더 크다면, A,B 모두 인덱스 +1, 아니라면 B만 +1
            answer += 1
            a += 1
        b += 1
        
    return answer
# 프로그래머스
# B가 최대 승점으로 이기는 승점 구하기

