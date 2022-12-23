import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

end = max(arr)
result = 0
def bS(s, e):
    global result
    while s <= e:
        total = 0
        mid = (s + e) // 2
        for x in arr:
            if x > mid:
                total += (x - mid)
        if total >= m:
            s = mid + 1
            result = mid
        else:
            e = mid - 1
    return result
print(bS(1, end))

