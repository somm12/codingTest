n, c = map(int,input().split())
h = []
for _ in range(n):
    h.append(int(input()))

h.sort()
s = 1
e = h[-1] - h[0]
result = 0
while s <= e:
    mid = (s+e)//2
    cnt = 1
    temp = h[0]
    for i in range(1,n):
        if temp + mid <= h[i]:
            temp = h[i]
            cnt += 1
    if cnt >= c:
        s = mid + 1
        result = mid
    else:
        e = mid -1
print(result)