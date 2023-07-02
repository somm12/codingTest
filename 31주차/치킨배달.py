from collections import deque
n,m = map(int,input().split())
board = []
house = []
chicken = []

for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] == 1:# 집들 좌표.
            house.append((i,j))
        elif board[i][j] == 2:# 치킨집 들 좌표.
            chicken.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]


answer = int(1e9)

def chooseM():# 남겨줄 치킨 집 m개가 되는 모든 경우의 수 반환.
    arr = []
    def dfs(L,start,res):
        if L == m:
            arr.append(res)
            return 
        for i in range(start, len(chicken)):
            dfs(L+1, i+1, res+[chicken[i]]) 
    dfs(0,0,[])
    return arr

for arr in chooseM(): # 남겨둔 치킨 집 m개
    total = 0 # 도시 치킨 거리
    for x,y in house: # 집들의 좌표
        d =int(1e9)
        for i,j in arr: # 각 집의 치킨 집 거리 구하기.
            d = min(d, abs(x-i)+abs(y-j))
        total += d # 하나씩 더해서 도시 치킨 거리를 구한다.
    answer = min(answer,total) # 도시 치킨 거리 최솟값 구하기.
print(answer)