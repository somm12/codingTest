import heapq
def solution(n, works):
    answer = 0
    q = []
    for v in works:
        heapq.heappush(q,-v)
    while n > 0 and q:
        v = heapq.heappop(q)
        if v + 1 != 0:
            heapq.heappush(q,v+1)
        n -= 1
    for v in q:
        answer+= (v**2)
    return answer
# 프로그래머스 lv3 문제
# 가장 큰 수를 가진 작업부터 해결해나가기