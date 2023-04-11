n = int(input())
arr = [i for i in range(1,n+1)]
step = 1
while len(arr) > 1:
    idx =((step)**3 % len(arr)) - 1
    if idx < 0:
        idx += len(arr)
    arr = arr[idx+1:] + arr[:idx]
    step += 1
print(arr[0])
