n,m = map(int,input().split())
house =[]
chicken = []

g = []
answer = int(1e9)
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 1:
            house.append((i,j))
        elif g[i][j] == 2:
            chicken.append((i,j))
            

def dfs(tmp,start):# 최대 m개의 치킨집을 폐업시키지 X을 때의 치킨 집 최소거리 => 치킨집이 많아야 최소거리가 나오므로 m개 뽑으면 된다.
    global answer
    if len(tmp) == m:
        answer = min(answer,chickenDist(tmp))
        return
    for i in range(start, len(chicken)):
        dfs(tmp + [chicken[i]],i+1)

   

def chickenDist(store):
    total = 0
    for x,y in house:
        minV = int(1e9)# 각 집의 치킨거리 구하기.
        for tx,ty in store:
            minV = min(minV,abs(tx-x)+abs(ty-y))
        total += minV# 도시 치킨거리 구하기
    return total


dfs([],0)

print(answer)

        