n = int(input())
arr = []
for _ in range(n):
    a, b = input().split()
    arr.append([a,int(b)])
arr.sort(key=lambda x: (x[1],x[0]))

for i in arr:
    print(i[0], end='')