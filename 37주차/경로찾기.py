n = int(input())
g = []

for i in range(n):
    g.append(list(map(int,input().split())))
   
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] != 0 and g[k][j] != 0:
                g[i][j] = 1
for i in range(n):
    for j in range(n):
        print(g[i][j], end=' ')
    print()
# 백준 최단거리 문제