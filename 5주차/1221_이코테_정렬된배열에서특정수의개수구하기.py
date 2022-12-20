from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
n, x = map(int, input().split())
arr = list(map(int, input().split()))

a = bisect_left(arr,x)
b = bisect_right(arr,x)

if a == b:
    print(-1)
else:
     print(b-a)