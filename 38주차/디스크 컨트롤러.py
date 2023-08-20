import heapq

def solution(jobs):
  
    h = []
    answer, now, i = 0, 0, 0
    # 이전 시점에서 가능했던 모단 작업을 힙에 할당한 시간.
    prevTime = -1
    # 현시점에서 가능한 작업을 고르고, 그 중 가장 소요시간이 짧은 것 먼저 처리 
    while i < len(jobs) :# 한개씩 작업 처리.
        for job in jobs:
            # 요청 시간이 이전 시점에서 힙에 할당한 시간 보다 커야함. 중복 제외!
            # 현재 시간보다 작거나 같은 작업을 최소 힙에 push
            if prevTime < job[0] <= now:
                # 소요 시간이 작은 작업이 우선적으로 처리.
                heapq.heappush(h, [job[1], job[0]])
        if len(h) > 0:# 현시점에서 할 수 있는 작업이 존재한다면,
            time, reqTime = heapq.heappop(h)# 소요시간, 요청 시간.
            # 이전 작업의 시작 시간을 현재 시간으로 갱신
            prevTime = now
            # 현재 시간에 작업 소요 시간을 더해 현재 시간 갱신
            now += time
            #대기 시간 및 처리시간 누적
            answer += (now - reqTime)
            i += 1# 한개 작업 처리.
        else:
            # 힙이 비어있는 상태라면 작업을 받기 위해 현재 시간 1증가
            now += 1
    return answer//len(jobs)
# 프로그래머스 lv3 문제.