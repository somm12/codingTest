def solution(n,times):
    answer = 0
    minTime = min(times)# 최대 범위.
    s = 1
    e = n*minTime
    while s<= e:
        mid = (s+e)//2 # mid만큼의 시간동안 몇 명이 심사 받을 수 있는지 체크.
        p = 0
        for t in times:
            p += (mid//t)
        if p >= n: # n명이상이라면, 범위를 더 좁히고, answer에 넣기.
            answer = mid
            e = mid-1
        else:
            s = mid+1
    return answer
# 프로그래머스 
# 이분탐색