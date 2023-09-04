import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(key=lambda x:(x[1]))# 소요시간 짧은 기준 정렬.
    now = 0
    while jobs:
        for i in range(len(jobs)):# 현재 시점에서 처리가 가능한 job이 있다면 처리.
            if now >= jobs[i][0]:
                now += jobs[i][1]# 처리하고 now 시간 update
                answer += now-jobs[i][0] # 걸린시간 더하기.
                jobs.pop(i)# 해당 job pop하고 break.
                break
            if i == len(jobs)-1:# 만약 아무도 해당 시점에 처리를 못한다면 +1
                now += 1
    
    return answer//n
# 프로그래머스 lv3 문제.
# 현재 시점에서 가장 소요시간이 적은 것 하나씩 처리.