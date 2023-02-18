import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    summary = 0
    previous = 0
    length = len(food_times)
    while summary + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        summary += (now-previous) * length
        length -= 1
        previous = now
    q.sort(key=lambda x:x[1])
    return q[(k-summary)%length][1]
print(solution([3,1,2],5))