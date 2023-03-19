import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        v1 = heapq.heappop(scoville)
        if v1 >= K:
            return answer
        if scoville:
            v2 = heapq.heappop(scoville)
            tmp = v1 + (v2*2)
            heapq.heappush(scoville,tmp)
            answer += 1
    
    return -1
# 더 맵게