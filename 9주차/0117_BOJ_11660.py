import sys
input = sys.stdin.readline
n,m = map(int, input().split())
table = [[0]*(n+1)]
prefix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    table.append([0]+list(map(int, input().split())))
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        temp += table[i][j]
        prefix[i][j] = temp
for j in range(1,n+1):
    temp = 0
    for i in range(1,1+n):
        temp += prefix[i][j]
        prefix[i][j] = temp
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x2][y1-1]-prefix[x1-1][y2]+prefix[x1-1][y1-1])

