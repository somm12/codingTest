arr = []

M = int(input())
N = int(input())

def check(n):
    for i in range(1, int(n**0.5) + 1):
        if n/i == i:
            arr.append(n)
            break

for i in range(M,N+1):
    check(i)
if len(arr) == 0:
    print(-1)
else:
    arr.sort()
    print(sum(arr))
    print(arr[0])
