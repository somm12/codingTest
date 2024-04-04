
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        l,r = 0,0
        dict = defaultdict(int)
        n = len(s)
        while r < n:
            if dict[s[r]] == 0:# 아직 문자가 0개라면 추가.
                dict[s[r]] += 1
                r += 1
                answer = max(answer,r-l)
            else:# 이미 문자가 존재하면 l를 증가시키면서, 범위를 줄여나가기.
                dict[s[l]] -= 1
                l += 1
        return answer

        
# leetcode: Longest Substring Without Repeating Characters