n,k = map(int,input().split())
arr = list(map(int,input().split()))

e = 0
odd = 0
even= 0
answer = 0
for start in range(n):
    while e < n and odd <= k:
        if arr[e] % 2 ==0:
            even += 1
        else:
            odd += 1
        e += 1
    answer = max(answer,even)
    if arr[start]%2 == 0:
        even -= 1
    else:
        odd -= 1
print(answer)