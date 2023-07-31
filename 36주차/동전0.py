answer =0
n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for v in arr:
    if k >= v:
    
        answer += (k//v)
        k %= v
print(answer)