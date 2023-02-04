import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

ans = 1

def bs(s,e):
    global ans
    while s <= e:
        mid = (s+e)//2
        cnt = 1
        d = arr[0] + mid
        for i in range(1,n):
            if d <= arr[i]:
                cnt += 1
                d = arr[i] + mid
        if cnt < c:
            e = mid - 1
        else:
            s = mid + 1
            ans = max(ans,mid)
bs(1,arr[n-1]-arr[0])
print(ans)