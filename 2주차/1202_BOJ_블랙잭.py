n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = -1
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            total = arr[i] + arr[j] + arr[k]
            if total <= m:
                ans = max(ans, total)
print(ans)
