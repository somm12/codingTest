import heapq
n = int(input())
arr = []
q = []
for _ in range(n):
    a = int(input())
    heapq.heappush(q,a)
    
answer = 0


while len(q)!=1:# 1개가 남으면 더이상 묶는 것 종료.
    first = heapq.heappop(q)
    
    second = heapq.heappop(q)
    tmp = first+second
    answer += (tmp)
    heapq.heappush(q,tmp)
print(answer)

# 백준 카드정렬하기 문제
# 총 카드 묶음 합이 최소로 나와야하므로, 매번 최소인 수 두 개를 더해나가야함.
# 힙을 사용하는 것이 핵심.