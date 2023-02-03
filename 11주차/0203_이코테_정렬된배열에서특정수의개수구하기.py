from bisect import bisect_right,bisect_left

n, x = map(int,input().split())
arr = list(map(int, input().split()))

l = bisect_left(arr,x)
e = bisect_right(arr,x)

if e - l > 0:
    print(e-l)
else:
    print(-1)