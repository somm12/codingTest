n,x = map(int,input().split())
arr = list(map(int,input().split()))
tmp = [0]
total = 0
for v in arr:
    total += v
    tmp.append(total)

maxV = 0
for i in range(n-x+1):
    maxV = max(maxV, tmp[i+x]-tmp[i])

cnt = 0
for i in range(n-x+1):
    if tmp[i+x] - tmp[i] == maxV:
        cnt += 1

if maxV == 0:
    print('SAD')
else:
    print(maxV)
    print(cnt)

# 다른 풀이: 슬라이딩 윈도우.

if max(arr) == 0:
    print('SAD')
else:
    midSum = sum(arr[:x])
    maxV = midSum
    cnt = 1
    for i in range(x,n):
        midSum += arr[i]
        midSum -= arr[i-x]
        if maxV < midSum:
            maxV = midSum
            cnt =1
        elif maxV == midSum:
            cnt += 1
    print(maxV)
    print(cnt)
