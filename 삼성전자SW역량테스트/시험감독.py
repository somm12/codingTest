n = int(input())
arr = list(map(int,input().split()))
B,C = map(int,input().split())
ans = 0
for p in arr:
    ans += 1
    if p - B > 0:
        if (p-B) % C != 0:
            ans += (p-B) // C + 1
        else:
            ans += (p-B) // C
print(ans)