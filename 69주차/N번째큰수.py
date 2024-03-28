import heapq
q= []
n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    for v in arr:
        heapq.heappush(q,v)
        if len(q) > n:# 힙의 크기가 n이 되도록 유지. -> 마지막에는 제일 큰 n개 수만 남고. 그 때의 힙의 첫번째 원소는 N번째 큰 원소.
            heapq.heappop(q)
        
    
print(heapq.heappop(q))
# 메모리 제한 12MB
# 모든 수를 heap에 넣으면 메모리 초과.