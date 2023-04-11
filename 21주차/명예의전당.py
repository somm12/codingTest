import heapq
def solution(k,score):
    answer = []
    q = []
    for i,v in enumerate(score):
        if i < k:
            heapq.heappush(q,v)
        else:
            if q[0] < v:
                heapq.heappop(q)
                heapq.heappush(q,v)
        answer.append(q[0])
    return answer
    