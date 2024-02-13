n = int(input())
nums = list(map(int, input().split()))

prefix_sum = 0
res = 0
for i in range(len(nums) - 1, 0, -1):
    prefix_sum += nums[i]
    res += nums[i - 1] * prefix_sum

print(res)

# x1x2 + x1x3 + x1x4 + x1x5,,, xn-1xn
# => x1(x2+x3+,,+xn)+ x2(x3+x4,,) +  .. +xn-1(xn)
