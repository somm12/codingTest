import copy
n,m = map(int,input().split())

room = [] # 사무실 그래프를 담을 배열.
cctvList = [] # 모든 cctv 위치를 담을 배열.
answer = 64 # 최소 사각지대 구하기 위해, 최대값 64. (n,m은 8이 최대)
# 각 cctv의 종류에 따라 가질 수 있는 방향들.
cctv = [[],[[0],[1],[2],[3]], [[0,1], [2,3]], [[0,3], [1,3], [1,2], [0,2]], [[0,1,2], [0,1,3], [0,2,3],[1,2,3]], [[0,1,2,3]]      ]
dx = [-1,1,0,0]# 상 하 좌 우.
dy = [0,0,-1,1] 

for i in range(n):
    room.append((list(map(int,input().split()))))
    for j in range(m):
        if 1 <= room[i][j] <= 5: # cctv라면, 위치를 담기.
            cctvList.append((i,j))

def watch(direction, copied): # 감시 시작.
    for i,v in enumerate(direction): # 모든 cctv가 정해진 방향대로 감시 시작.
        for d in v: # v (각 cctv가 가진 방향들을 가짐.)
            nx = cctvList[i][0] # cctv 하나씩 현재 위치에서 감시.
            ny = cctvList[i][1]
            while True:
                nx += dx[d] # 해당 방향으로 감시, 벽을 만나거나 범위를 벗어나면 break.
                ny += dy[d]
                if 0<= nx < n and 0 <= ny < m:
                    if copied[nx][ny] == 6: # 벽을 만나면 감시 불가.
                        break
                    if copied[nx][ny] == 0:
                        copied[nx][ny] = -1
                else:
                    break
    
    return copied

def area(tmp): # 사각지대 구하기.
    global answer
    cnt  = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1    
    answer = min(answer,cnt)

def dfs(L,res):
    if L == len(cctvList):
        tmp = copy.deepcopy(room)
        tmp = watch(res,tmp)
        area(tmp)
        return 
    
    x = cctvList[L][0] # 현재 depth의 cctv의 x,y좌표.
    y = cctvList[L][1]

    for direction in cctv[room[x][y]]: # 해당 cctv 타입이 가질 수 있는 방향 하나 선택.
        res.append(direction) # res에 append
        dfs(L+1, res) 
        res.pop() # 재귀가 끝나면 pop으로 이전까지 했던 경우로 돌아감.
dfs(0,[])
print(answer)