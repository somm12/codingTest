import heapq

n = int(input())
arr = []
q = []
for _ in range(n):
    p,d = map(int,input().split())
    arr.append((p,d))

arr.sort(key= lambda x : x[1])# day가 작은순으로 정렬.

for p,d in arr:
    heapq.heappush(q,p)# d일 안에 방문하는 것이므로, 현재 d일 내에 요청들 중, 큰 가격만 힙에 남기는 것!
    if len(q) > d:# d일 보다 힙 크기가 더 커진다면, 작은 값을 뺀다. -> 마지막에는 큰 것만 남음.
        heapq.heappop(q)
        

answer = 0
while q:
    p= heapq.heappop(q)
    answer += p
print(answer)
# 백준 순회강연
# 최대값 -> 최소를 작게 포함하자.