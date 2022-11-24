n = int(input())
btn = [300, 60, 10]
ans = []
if n % 10 != 0:
    print(-1)
else:
    for v in btn:
        ans.append( n // v)
        n = n % v
    for i in ans:
        print(i, end=' ')