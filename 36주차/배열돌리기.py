T = int(input())
import copy
def clock():
    global g, n
    new = copy.deepcopy(g)
    leftCross =[]
    for i in range(n):
        leftCross.append(g[i][i])
    for i in range(n):
        new[i][n//2] = leftCross[i]
    
    midCol = []
    for i in range(n):
        midCol.append(g[i][n//2])
    for i in range(n):
        new[i][n-1-i] = midCol[i]
    
    rightCross = []

    for i in range(n):
        rightCross.append(g[n-1-i][i])
    for i in range(n):
        new[n//2][i] = rightCross[i]
    
    midRow = []
    for i in range(n):
        midRow.append(g[n//2][i])
    for i in range(n):
        new[i][i] = midRow[i]
    g = new



for _ in range(T):
    n,d = map(int,input().split())
    g = []
    for _ in range(n):
        g.append(list(map(int,input().split())))
    if d < 0:
        times = (d*-1)//45
        for _ in range(8-times):
            clock()
    else:
        times = d//45
        for _ in range(times):
            clock()
    
    for i in range(n):
        for j in range(n):
            print(g[i][j],end=' ')
        print()
# 백준 구현 문제.