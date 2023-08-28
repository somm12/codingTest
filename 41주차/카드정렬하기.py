import heapq

q =[]
n = int(input())

for _ in range(n):
    heapq.heappush(q,int(input()))
answer = 0
while len(q) != 1:
    v1 = heapq.heappop(q)
    v2 = heapq.heappop(q)
    tmp = (v1+v2)
    answer += tmp
    heapq.heappush(q,tmp)

print(answer)
# 카드 묶음을 하나로 합치기.
# 묶는데 드는 비용을 구한다.
# 가장 적은 묶음 끼리 두 개씩 묶기 => heap 사용.