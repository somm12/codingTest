import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict ={}
        answer = []
        maxheap = []
        for v in nums:
            if v not in dict:
                dict[v] = 1
            else:
                dict[v] += 1
        
        for v in dict:
            heapq.heappush(maxheap,(dict[v]*-1, v))
        for _ in range(k):
            answer.append(heapq.heappop(maxheap)[1])
        return answer
        

# leetcode : Top K Frequent Elements 
# 가장 개수가 많은 k개의 원소 반환.