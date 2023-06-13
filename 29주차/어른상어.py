n,m,k = map(int,input().split())
shark = [[]*n for _ in range(n)] # 상어의 위치를 담을 3차원 배열.
smell = [[] *n for _ in range(n)] # 상어 냄새 정보를 담을 3차원 배열. [[[상어번호, 남은 시간]]]
dx=[-1,1,0,0] # 상 하 좌 우.
dy=[0,0,-1,1]

# p[nth][d][0...3] => 1번 상어가 d방향일때의 우선순위(0,1,2,3 중 하나).
p = [[] for _ in range(m+1)]  # 각 상어들의 현재 방향에 따른 우선순위 방향을 담은 배열.
di = [0] # 상어 현재 방향. 각 x번 상어의 방향.
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n):
        if a[j] != 0:
            shark[i].append([a[j]]) # 나중에 한 칸당 상어가 여러개 올 수 있으므로, 3차원배열 사용.
        else:
            shark[i].append([]) # 없으면 빈배열로 추가.
        smell[i].append([0,0]) # 냄새 배열 초기화.
tmp = list(map(int,input().split()))
for i in tmp: # 현재 상어들의 방향.
    di.append(i-1)
for i in range(1,m+1):# m 개의 상어 이동방향 우선순위 입력받기.
    for _ in range(4):
        a,b,c,d = map(int,input().split())
        tmp = [a-1,b-1,c-1,d-1]
        p[i].append(tmp) # i번 상어의 우선순위 배열 추가.

# 상어 냄새 뿌리기.
def spread():
    global smell
    for i in range(n):
        for j in range(n):
            if len(shark[i][j]) != 0: # 현재 상어가 있는 위치에서 뿌린다.
                num = shark[i][j][0]
                smell[i][j] = [num,k]
# 상어의 이동.
def move():
    global shark
    new = [[[] for _ in range(n)] for _ in range(n)] # 이동 이후 모습을 담을 3차원 배열.
    for i in range(n):
        for j in range(n):
            if len(shark[i][j]) != 0: # 상어가 존재한다면
                num = shark[i][j][0]
                to = [] # 아무 냄새가 없는 칸으로 이동 가능한 좌표를 담을 배열
                mine = [] # 냄새가 없는 칸이 없을 때, 자신의 냄새가 있는 칸 좌표를 담을 배열.
                for d in p[num][di[num]]:# num번 상어의 현재 방향이 di[num]일때의 우선순위.
                    nx = i+dx[d]
                    ny = j+dy[d]
                    if 0<= nx < n and 0 <= ny < n:# 범위를 벗어나지 않고.
                        if smell[nx][ny] == [0,0]:# 아무냄새 없는 칸일때.
                            to.append((nx,ny,d))
                        elif smell[nx][ny][0] == num: # 자신의 냄새 칸일때.
                            mine.append((nx,ny,d))
                if len(to) > 0: # 아무 냄새 없는 칸 좌표가 있다면 그곳으로 이동,
                    x,y,d = to[0]
                elif len(mine) > 0:
                    x,y,d = mine[0]
                new[x][y].append(num) # 이동 후, 상어가 바라보는 방향도 변경!!!!**
                di[num] = d
    shark = new # 이동 후의 상어 위치 갱신


def remove():# 한칸에 여러개 상어가 있다면 제일 번호가 작은 상어만 남기고 제거.
    global shark
    for i in range(n):
        for j in range(n):
            if len(shark[i][j]) > 1:
                v = min(shark[i][j])
                shark[i][j] = [v]

def check(): # 상어가 1번 하나만 남았는지 확인.
    total = 0
    for i in range(n):
        for j in range(n):
            if len(shark[i][j]) > 0:
                total += 1
    if total == 1:
        return True
    return False

def reduceT(): # 이동 이후, 남은 냄새들의 시간을 1초 줄인다.
    global smell
    for i in range(n):
        for j in range(n):
            if smell[i][j] != [0,0]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0: # 0초가 되면 냄새 제거.
                    smell[i][j] = [0,0]

for T in range(1,1001):
   
    spread()
    move()
    remove()
    if check():
        print(T)
        break
    reduceT()
else: # 1000초 넘게 이동해도 안되면 -1
    print(-1)
