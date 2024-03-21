def solution(n, cores):
    answer = 0
    
    n -= len(cores)# 맨 처음에 모든 코어는 작업을 할당 받음.
    if n <= 0:# 이미 남은 작업수가 없다면. n번째 코어가 마지막 작업 처리.
        return n
    maxV = max(cores)*n
    s,e= 0,maxV# 0초대 ~ 마지막 최대 시간(걸리는 작업 시간)
    
    while s<=e:# 이분 탐색으로 마지막 작업을 처리하는 시간대 찾기.
        mid = (s+e)//2
        total = 0
        for c in cores:
            if c == 0:
                continue
            total += (mid//c)
        if total >= n:# 거리 좁히기
            e = mid-1
            last =mid# 모든 작업을 처리하는 시간대 저장.
            
        else:
            s = mid+1
    
    prevTotal = 0
    
    for v in cores:
        if v == 0:
            continue
        prevTotal += (last-1)//v# 마지막 작업 처리 시간 이전 까지의 작업을 모두 빼주기.
   
    remain = n-prevTotal# 마지막 시간에서의! 남은 작업 개수
    
    for i,v in enumerate(cores):
        if v == 0: continue
        if last % v == 0:# 시간/코어 처리 시간. 나누어 떨어진다면 해당 시간대 작업을 처리한다는 말.
            remain -= 1
            if remain == 0:# 0 이 되는 순간 == 마지막 작업 처리.
                answer = i+1
                break
        
    
    return answer