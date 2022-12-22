import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
end = max(arr)
result = 0
def biS(s, e):
    global result
    while s <= e:
        count = 0
        mid = (s+e)//2
        
        for x in arr:
            count += (x // mid)
        if count >= n:
            result = mid
            s = mid + 1
        else:
            e = mid - 1
    return result

print(biS(1, end)) 
