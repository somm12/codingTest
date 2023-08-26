def solution(sequence):
    answer = 0
    tmp = 1
    arr =[]
    n = len(sequence)
    for v in sequence: # 펄스 수열 곱하기
        arr.append(tmp*v)
        tmp *= -1
    total = [0]*(n+1)
    for i in range(1,n+1):# 구간합 구하기
        total[i] = total[i-1] + arr[i-1]
    return max(total)-min(total)
# 프로그래머스 문제
# 정확히 부호가 반대이므로, 누적합 결과과 부호가 반대이다. 
# a가 있다는 것은 -a가 존재한다는 것.
# 1,-1,1,-1,, 경우만 고려해서 구간합을 구하고, 최대값-최솟값을 구해줘도 됨.