import sys
input = sys.stdin.readline
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

k = int(input())

total = [[0]*(m+1) for _ in range(n+1)]

for x in range(1,n+1):
    for y in range(1,m+1):
        total[x][y] = g[x-1][y-1] + total[x-1][y] + total[x][y-1] - total[x-1][y-1]


for _ in range(k):
    i,j,x,y = map(int,input().split())
    v = total[x][y] - (total[x][j-1] + total[i-1][y]) + total[i-1][j-1]
    print(v)