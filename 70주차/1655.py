import heapq
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

minheap = []
maxheap = []
mid = arr[0]
answer = []
answer.append(mid)

for i in range(1,n):
    value = arr[i]
    if i % 2 == 1:# 이전까지 홀수개 였다면, => 이제 짝수개 되니까 두 개 중 작은 중간값(최대힙에서)을 선택.
        if value > mid:# 중간 값보다 크다면, 최대힙으로 새로운 값을 넣고, mid는 최소힙.
            heapq.heappush(minheap,value)
            heapq.heappush(maxheap,mid*-1)
        else:
            heapq.heappush(maxheap,value*-1)
            heapq.heappush(minheap,mid)
        answer.append(maxheap[0]*-1)
    else:# 이제 홀수개가 된다면, 새로운 값이 최소힙의 최소값보다 작으면,최대힙에 새로운 값을 넣고, 빼서 Mid를 만든다.
        if value < minheap[0]:
            heapq.heappush(maxheap,value*-1)
            mid = heapq.heappop(maxheap)*-1
        else:
            heapq.heappush(minheap,value)
            mid = heapq.heappop(minheap)
        answer.append(mid) # 홀수개라 중간 값이 나오므로 append

for v in answer:
    print(v)