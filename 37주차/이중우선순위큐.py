import heapq 

def solution(operations):
    answer = []
    q = []

    for com in operations:
        a,num = com.split()
        num = int(num)
        
        if a == 'I':
            heapq.heappush(q,num)
            
        else:
            if q:
                if num == 1:
                    q = heapq.nlargest(len(q),q)[1:]# nlargest(a,b): 배열 b 에서 a개의 가장 큰 요소들을 리스트로 반환.
                    heapq.heapify(q)
                else:
                    heapq.heappop(q)
    
    if not q:
        return [0,0]
        
    return [heapq.nlargest(1,q)[0], heapq.heappop(q)]
# 프로그래머스 lv3 문제
# 매번 sort()를 사용해서 문제를 풀어볼 수도 있다.