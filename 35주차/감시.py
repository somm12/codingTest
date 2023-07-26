import copy
n,m = map(int,input().split())
room = []
cctvList= []
dx=[-1,1,0,0]# 상하좌우
dy = [0,0,-1,1]

for i in range(n):
    room.append(list(map(int,input().split())))
    for j in range(m):
        if 1<= room[i][j] <= 5:
            cctvList.append((i,j))# cctv좌표 담기.
# 각 1~5번 cctv들이 가질 수 있는 방향 리스트.
cctvDirection = [[], [[0], [1], [2], [3]], [[0,1],[2,3]],
                [[0,3], [1,3], [1,2], [0,2]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3] ],
                [[0,1,2,3]] ]

answer = 64 # 최대 사각지대 64(8*8)

def area(res):# 정해진 방향대로 cctv 감시 시작, 사각지대 구하기.
    temp =  copy.deepcopy(room)
    
    for i,arr in enumerate(res):
        x,y = cctvList[i]
       
        for d in arr:
            nx = x # 각각 한방향이 감시. nx,ny 변수를 써서, 한뱡으로 쭉 감시.
            ny = y
            while True:# 벽이나 범위 밖을 마주칠때까지. 감시.
                nx += dx[d]
                ny += dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if temp[nx][ny] == 6:# 벽이면 감시 멈춤.
                        break
                    elif temp[nx][ny] == 0:# 빈칸이면 #을 넣어서 사각지대에서 제외
                        temp[nx][ny] = '#'
                else:
                    break
    cnt = 0
   # 사각지대 구하기.
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def dfs(L,res):# 각 cctv가 가질 수 있는 방향 구하기.
    global answer
    if L == len(cctvList):# 각 cctv들이 방향이 정해지면, 사각지대를 구하는 area호출.
        answer = min(answer,area(res)) # 최소 사각지대를 구함
        return
    
    x,y= cctvList[L]# 현재 cctvList에서의 index에서 각 x,y좌표.
    for arr in cctvDirection[room[x][y]]:# 해당 cctv가 가질 수 있는 방향 조합 arr를 고른다.
        res.append(arr)
        dfs(L+1,res)
        res.pop()# 백트래킹.
dfs(0,[])
print(answer)
