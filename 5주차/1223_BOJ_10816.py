from bisect import bisect_left, bisect_right
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
arr.sort()

for x in a:
    print(bisect_right(arr, x) - bisect_left(arr,x),end=' ')
