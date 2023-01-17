import sys
input = sys.stdin.readline
n, m = map(int, input().split())
table = [[0]*(m+1)]
prefix = [[0]*(m+1) for _ in range(n+1)]
for _ in range(n):
    table.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
    t = 0
    for j in range(1, m+1):
        t += table[i][j]
        prefix[i][j] = t
for j in range(1,m+1):
    t = 0
    for i in range(1,n+1):
        t += prefix[i][j]
        prefix[i][j] = t

k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    print(prefix[x][y]- prefix[x][j-1]- prefix[i-1][y]+prefix[i-1][j-1])
