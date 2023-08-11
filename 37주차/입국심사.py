def solution(n, times):
    answer = 0
    start = 0
    end = n*max(times)# 최대로 걸리는 시간까지 범위로 두기.
    
    while start <= end:
        mid = (start+end)//2
        people = 0
        for time in times:
            people += (mid//time)# 해당 시간 동안 검사할 수 있는 사람 총 몇명인지 구하기.
            if people >= n:
                break
        if people >= n:# 모두 심사가 가능 하다면, 점점 범위를 줄여나감.
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer
# 이분탐색.