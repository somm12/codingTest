maxV = -1
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
for row in arr:
    minV = min(row)
    maxV = max(minV,maxV)
print(maxV)