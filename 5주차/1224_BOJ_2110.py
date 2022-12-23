import sys
input = sys.stdin.readline
n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = 0
arr.sort()
def sol(s, e):
    global result
    while s <= e:
        cnt = 1
        current = arr[0]
        mid = (s+e)//2
        for i in range(1, n):
            if arr[i] >= current + mid:
                current = arr[i]
                cnt += 1
        if cnt >= c:
            result = mid
            s = mid + 1
        else:
            e = mid - 1

    return result

    
print(sol(1,arr[-1] - arr[0]))
