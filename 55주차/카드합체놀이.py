import heapq

n,m = map(int,input().split())
arr = list(map(int,input().split()))
q = []
for v in arr:
    heapq.heappush(q,v)

for _ in range(m):
    v1 = heapq.heappop(q)# 가장 작은 두개 숫자 꺼내기
    v2 = heapq.heappop(q)
    heapq.heappush(q,v1+v2)# 합을 다시 넣기(덮어쓰는 과정)
    heapq.heappush(q,v1+v2)

answer = 0
while q:# 총합.
    answer += heapq.heappop(q)
print(answer)