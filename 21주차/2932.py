from collections import deque
n,k = map(int,input().split())
arr = [[0]*n for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        arr[i][j]  = cnt
        cnt += 1
def locate(num):
    for i in range(n):
        for j in range(n):
            if num == arr[i][j]:
                return (i,j)

for _ in range(k):
    X,R,C = map(int,input().split())
    R -= 1
    C -= 1
    x,y = locate(X)
    a = R-x
    if a < 0:
        a = n + R-x
    b = C-y
    if b < 0:
        b = n + C-y
    answer = a + b

    tmp = deque(arr[x])
    times = C-y
    if times < 0:
        times = n + C-y
    tmp.rotate(times)
    arr[x] = list(tmp)
    t = deque()
    for i in range(n):
        t.append(arr[i][C])
    times = R-x
    if times < 0:
        times = n + R-x
    t.rotate(times)

    for i in range(n):
        arr[i][C] = t[i]
    print(answer)
