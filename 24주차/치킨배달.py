def combi(L,start,res):
    global answer
    if L == m:
        total = 0
        for x,y in house:
            tmp = int(1e9)
            for i,j in res:
                tmp = min(tmp, abs(x-i) + abs(y-j))
            total += tmp
        answer = min(answer,total)
        return 

    for i in range(start,len(chicken)):
        combi(L+1,i+1,res+[(chicken[i][0],chicken[i][1])])
    
n, m = map(int,input().split())
g = []
house = []
chicken = []
answer = int(1e9)
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 1:
            house.append((i,j))
        elif g[i][j] == 2:
            chicken.append((i,j))

combi(0,0,[])
print(answer)
