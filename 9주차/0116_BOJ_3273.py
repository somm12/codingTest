n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
s = 0
e = n - 1
arr.sort()
while s < e:
    inS = arr[s] + arr[e]
    if inS < x:
        s += 1
        continue
    if inS == x:
        cnt += 1
    e -=1
print(cnt)