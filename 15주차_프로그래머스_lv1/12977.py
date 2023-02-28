from itertools import combinations
import math 
def solution(nums):
    answer = 0
    for arr in list(combinations(nums,3)):
        t = sum(arr)
        for i in range(2, int(math.sqrt(t)) + 1):
            if t % i == 0:
                break
        else:
            answer += 1

    return answer
# 소수 만들기