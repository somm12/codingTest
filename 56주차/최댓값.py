g = []
x,y =0,0
maxV = -1
for _ in range(9):
    g.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if maxV < g[i][j]:
            maxV = g[i][j]
            x,y = i,j
# 답이 두 개면 둘 중하나 출력.
print(maxV)
print(x+1,y+1)
