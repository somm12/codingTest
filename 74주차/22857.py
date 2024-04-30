n,k = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
end = 0
odd,even = 0,0

for start in range(n):
    while end < n and odd <= k:
        if arr[end] %2 == 0:
            even += 1
        else:
            odd += 1
        end += 1
        answer = max(answer,even)
    if arr[start]% 2 == 0:
        even -=1
    else:
        odd -= 1
print(answer)
