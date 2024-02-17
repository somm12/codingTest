n,m = map(int,input().split())
g = [[0]*(m+1)]
for _ in range(n):
    g.append([0]+list(map(int,input().split())))

for x in range(1,n+1):
    for y in range(2,m+1):
        g[x][y] += g[x][y-1]
for y in range(1,m+1):
    for x in range(2,n+1):
        g[x][y] += g[x-1][y]
# g[x][y] : 1,1 ~ x,y까지의 합 담기


k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    # i,j ~ x,y 까지의 합. g[i-1][j-1]는 두번 제거 되므로 다시 더해야함.
    print(g[x][y] - (g[x][j-1] + g[i-1][y]) + g[i-1][j-1]) # 구간 및 누적 합. 
