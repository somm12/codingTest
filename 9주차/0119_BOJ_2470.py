n = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = 0
b = 0
res = 2 *(10**9)
s = 0
e = n-1
while s < e:
    total = arr[s] + arr[e]
    if total == 0:
        a = s
        b = e
        break
    if abs(total) < res:
        res = abs(total)
        a = s
        b = e
    if total < 0:
        s += 1
    else:
        e -= 1

print(arr[a],arr[b])