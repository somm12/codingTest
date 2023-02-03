n = int(input())
arr = list(map(int,input().split()))

def b(s,e):
    if s > e:
        return None
    mid = (s+e) // 2
    if mid == arr[mid]:
        return mid
    if mid > arr[mid]:
        return b(mid+1,e)
    else:
        return b(s,mid-1)
res = b(0,n-1)
if res == None:
    print(-1)
else:
    print(res)
