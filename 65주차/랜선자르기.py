k,n = map(int,input().split())
arr =[]
for _ in range(k):
    arr.append(int(input()))
s,e = 1,max(arr)

answer =0
while s<=e:
    mid = (s+e)//2
    cnt =0
    for v in arr:
        cnt += (v//mid)
    if cnt >= n:
        s = mid + 1
        answer = mid
    else:
        e = mid - 1
print(answer)