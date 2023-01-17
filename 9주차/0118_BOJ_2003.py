n, m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
end = 0
s = 0
for start in range(n):
    while s < m and end < n:
        s += arr[end]
        end += 1
    if s == m:
        cnt += 1
    s -= arr[start]
print(cnt)