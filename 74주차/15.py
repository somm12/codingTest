class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        answer = {}
        results =[]
        for i in range(n-2):
            l,e = i+1,n-1
            if i > 0 and nums[i] == nums[i-1]:# 이전 값과 같다면 확인하지 말고 넘기기.
                continue
            while l < e:
                total = nums[l] + nums[e]+nums[i]
                if total == 0:
                    answer[(nums[i],nums[l],nums[e])] = 1
                    l += 1
                elif total > 0:
                    e -= 1
                else:
                    l += 1
        results = answer.keys()
        return results
# leetcode. 3sum
        

        