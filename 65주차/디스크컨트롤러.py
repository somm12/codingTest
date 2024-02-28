import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    cnt = n
    jobs.sort()
    time = 0
    heap = []
    visited = [0]*n
    while cnt > 0:
        for i,v in enumerate(jobs):
            req,total = v
            if time >= req and not visited[i]:
                
                heapq.heappush(heap,[total, req])
                visited[i] = 1
     
        if heap:# 현재 처리할 수 있는 것 중 가장 짧은 일을 하기.
            total,req = heapq.heappop(heap)
            end = time + total
            answer += (end - req)
            time += total
            cnt -= 1
        else:# 처리할 수 있는 일이 없으면 시간만 +1
             time += 1
    
    return answer//n