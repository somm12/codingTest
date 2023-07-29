import copy
m,s = map(int,input().split()) # m마리 물고기수, s번 마법 시전.

dx = [0,-1,-1,-1,0,1,1,1]# 8가지 방향
dy = [-1,-1,0,1,1,1,0,-1]
mx = [-1,0,1,0] # 상어가 움직일 때 상하좌우 인접 방향.
my = [0,-1,0,1]

answer = 0
fish = [[[] for _ in range(4)] for _ in range(4)] # 각 좌표에 있는 물고기들의 방향 3차원배열
smell = [[[] for _ in range(4)] for _ in range(4)] # 각 좌표에 있는 물고기 냄새 3차원 배열.
for _ in range(m):
    fx,fy,d = map(int,input().split()) # 물고기 위치, 방향 입력 받기.
    fish[fx-1][fy-1].append(d-1)
sx,sy = map(int,input().split()) # 상어 위치.
sx -=1
sy -=1

def fishMove():# 물고기 이동. 가리키는 방향으로 이동할 수 있을 때 까지 반시계 45도 회전.
    global fish
    new = [[[] for _ in range(4)] for _ in range(4)]# 새로운 물고기 위치를 담을 배열.
    for x in range(4):
        for y in range(4):
            if len(fish[x][y]) > 0:# 물고기가 있다면
                for di in fish[x][y]: # 가리키는 방향으로 이동.
                    idx = di
                    for _ in range(8):
                    
                        nx = x+ dx[idx] #**
                        ny = y + dy[idx]
                        if 0 <= nx < 4 and 0 <= ny < 4 and len(smell[nx][ny]) == 0 and (nx,ny) != (sx,sy):
                            # 범위내, 물고기 냄새가 없고, 상어가 없는 칸이면 이동가능.
                            new[nx][ny].append(idx)
                            break
                        idx = (idx-1)%8# 반시계방향으로 이동(-1) 8로 나누어줌으로써, 0~7 방향 유지.
                    else:# 이동할 수 있는 칸이 없으면 그대로.
                        new[x][y].append(di)
    fish = new # 물고기 위치 업데이트
def choose(total,res):# 상어가 연속으로 3번 움직일 경우 구하기. (중복 순열.)
    global cand 
    if total == 3: # 3개가 되면
        removedCnt = go(res) # 해당 방향으로 움직일 수 있는지 체크.
        tmp = ''
        for i in res:
            tmp += str(i) # 방향 사전순으로 선택해야하므로, str를 이용해서 한 문자열 만들기.
        if removedCnt != -1:# 갈 수 있는 방향일 때, 후보자 배열에 append
            cand.append((removedCnt,tmp))
        return
    for i in range(4):
        choose(total+1, res+[i])

def go(res):# res에 담긴 배열 방향으로 상어가 움직일 수 있는지 체크.
    nx,ny= sx,sy
    cnt = 0
    
    visited = [[0]*4 for _ in range(4)]# 제거되는 물고기 수를 셀 때, 또 셀 수 있음을 방지하기 위함.
    for di in res:
        nx += mx[di]
        ny += my[di]
        if 0 <= nx < 4 and 0 <= ny < 4:# 범위 내고,
            if not visited[nx][ny]:# 상 하 하 와 같이 다시 방문했던 곳을 지나갈 수 있기 때문에, 제거되는 물고기 수를 셀 때만, 중복을 피한다.
                cnt += len(fish[nx][ny])
            visited[nx][ny] = 1 # 방문처리
        else:
            return -1 # 범위 밖은 -1 반환.
    return cnt # 제거되는 개수 반환.
def sharkMove(arr,nth):# 정해진 방향으로 상어 이동.
    global sx,sy,fish,smell
    nx,ny = sx,sy

    for di in arr:
        nx += mx[di]
        ny += my[di]
        if len(fish[nx][ny]) >0 :
            fish[nx][ny] = []# 물고기가 제거됨.
            smell[nx][ny].append(nth)# 제거되면서 냄새 남김.
    sx,sy = nx,ny # 상어 위치 업데이트.

def removeSmell(nth):# 두번 이전에 시전하면서 생겼던 냄새 없애기
    global smell
    
    for x in range(4): 
        for y in range(4):
            tmp = []
            for v in smell[x][y]:
                if v == nth -2: # 현재 nth번째 마법을 시전 중이라면, -2 번째 했던 냄새 없애기.
                    continue
                else:
                    tmp.append(v)
            smell[x][y] = tmp
        
def copyFish():# 복제했던 물고기 추가하기.
    global fish
    for x in range(4):
        for y in range(4):
            for v in copyied[x][y]:
                fish[x][y].append(v)

for nth in range(1,s+1):
    copyied = copy.deepcopy(fish) # 복제
    fishMove()# 이동
    cand = []# 상어가 이동할 방향을 담을 배열
    choose(0,[])# 상어가 이동할 3연속 방향 찾기.
    
    
    cand.sort(key=lambda x: (-x[0],x[1]))# 제거되는 물고기 수 많고 > 방향 사전순으로 정렬.
    arr = []
    for i in cand[0][1]:# 3연속 방향이 문자열 형태를 다시 정수 배열로 만들고
        arr.append(int(i))
    sharkMove(arr,nth) # 정한 방향으로 상어가 이동. 이동하면서 물고기제거&냄새 남김

    removeSmell(nth)# 냄새 제거
    copyFish()# 복제되었던 물고기 추가됨
 


for x in range(4):# 최종 남은 물고기수 세기
    for y in range(4):
        answer+= len(fish[x][y])
print(answer)