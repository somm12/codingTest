class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = int(1e9)
        answer =0 
        nums.sort()
        n = len(nums)        
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if diff > abs(total - target):
                    diff = abs(total - target)
                    answer =total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
        return answer
# leetcode: 3sum closet