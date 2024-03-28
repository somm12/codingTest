
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        dict = defaultdict(int)
        answer = 0
        l,r = 0,0
        while r < len(nums):
            
            if dict[nums[r]] >= k:
                dict[nums[l]] -= 1
                l += 1
            else:
                dict[nums[r]] += 1
                r += 1
    
            answer = max(answer, r-l)
  
    
        return answer
# leet code: Length of Longest Subarray With at Most K Frequency