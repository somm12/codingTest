import heapq
def solution(q, K):

    heapq.heapify(q)
    answer = 0
    while q:
        v1 = heapq.heappop(q)
        if v1>=K:
            return answer
        if q:
            v2 = heapq.heappop(q)
            heapq.heappush(q,v1+(v2*2))
            answer += 1
    
    return -1# 힙 원소가 없어질때까지 답이 구해지지 않으면 구할 수 없다는 것
# 프로그매러스 힙 문제.