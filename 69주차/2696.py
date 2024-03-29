import heapq
import math
t = int(input())
for _ in range(t):
    m = int(input())
    arr = []
  
    for _ in range(math.ceil(m/10)):
        for v in list(map(int,input().split())):
            arr.append(v)
    print((m+1)//2)
    mid = arr[0]
    result = [mid]
    maxheap = []
    minheap = []
       
    for i in range(1,m):
        new = arr[i]
        if i % 2 == 0:# 이전까지 짝수개 였다면, mid 중앙값을 설정.
            if new > minheap[0]:# 최소힙 값보다 크면, 최소힙의 값을 Pop 한 것이 mid
                mid = heapq.heappop(minheap)
                heapq.heappush(minheap,new)
            else: # 아니면 최대힙 pop 한 것이 Mid.
                heapq.heappush(maxheap,new*-1)
                mid = heapq.heappop(maxheap)
                mid *= -1
            
            result.append(mid)
        else:# 이전 까지 홀수 개였다면, mid 를 힙에 넣는다.
            if new > mid:# 새로운 값이 Mid 보다 크면 최소힙. mid는 최대힙.
                heapq.heappush(minheap,new)
                heapq.heappush(maxheap,mid*-1)
            else:
                heapq.heappush(maxheap,new*-1)
                heapq.heappush(minheap,mid)
    for i in range(len(result)):
        print(result[i],end =' ')
        if (i+1) % 10 == 0:
            print()  
    print()
# 최소힙과 최대힙을 이용하는 문제
# 최대힙 Mid 최소힙 => 입력 하나가 들어올 때마다 이를 최대한 유지하는 방법.