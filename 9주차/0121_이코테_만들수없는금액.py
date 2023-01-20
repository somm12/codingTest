n = input()
arr = list(map(int, input().split()))
arr.sort()
target = 1
for data in arr:
    if target < data:
        break
    target += data
print(target)

