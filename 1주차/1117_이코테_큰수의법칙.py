n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0
count = 0
for _ in range(m):
    if count < k:
        ans += arr[0]
        count += 1
    else:
        ans += arr[1]
        count = 0
print(ans)