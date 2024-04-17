n,s = map(int,input().split())
arr = list(map(int,input().split()))
total, e = 0,0
answer = int(1e9)
flag = False
for start in range(n):
    while total < s and e < n:
        total += arr[e]
        e += 1
    if total >= s:
        total -= arr[start]
        answer = min(answer, e-start)
        flag = True
if not flag:
    print(0)
else:
    print(answer)