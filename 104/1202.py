import heapq 
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = []# 보석
for _ in range(n):
    m,v = map(int,input().split())
    arr.append((m,v))
bags=[]
for _ in range(k):
    bags.append(int(input()))

bags.sort()
arr.sort()
answer = 0
hq= []

j= 0 
for i in range(k):# 현재 가방에 넣을 수 있는 보석 넣기.
    while j < n and arr[j][0]<= bags[i]: # 그 다음 가방에서는 자연스레 남은 넣을 수 있는 보석 중 비싼 것을 고를 수 있다.
        heapq.heappush(hq,arr[j][1]*-1)# 후에 가장 가격이 비싼 것 고르기 위해 힙에 넣기.
        j += 1
    
    if hq:# 가방에 보석은 최대 하나만 넣을 수 있기 때문에 한 번만 pop. 
        answer += (heapq.heappop(hq)*-1)
print(answer)
# 백준 보석 도둑. 그리디.