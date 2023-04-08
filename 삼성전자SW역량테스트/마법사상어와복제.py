from itertools import product
m,s = map(int,input().split())# 물고기 개수, 연습횟수
ori_fish = [] # 처음 입력한 물고기들 위치와 방향(x,y,d)
ori_cnt = [[0]*4 for _ in range(4)]# 처음 물고기 각 칸에 몇 개 존재인지

# 물고기 움직이는 방향 8개 ( 왼, 왼위, 위 .... 왼아래 시계방향 쪽으로냐열)
fx = [0,-1,-1,-1,0,1,1,1]
fy = [-1,-1,0,1,1,1,0,-1]

# 상어 움직이는 위치 상좌하
sx = [-1,0,1,0]
sy = [0,-1,0,1]
for _ in range(m):
    x,y,d = map(int,input().split())
    ori_fish.append((x-1,y-1,d-1))
    ori_cnt[x-1][y-1] += 1
# 상어가 움직일 수 있는 모든 방향 루트 64개.
r= list(product([0,1,2,3],repeat = 3))#### 중복 조합******

sharkx, sharky = map(int,input().split())
sharkx -=1
sharky -=1

time = 0
smell = {}

def move_fish():# 물고기 이동 후 위치 방향 배열 반
    new = []
    for x,y,d in ori_fish:

        tmpd = d
        for _ in range(8):
            nx = x + fx[tmpd]
            ny = y + fy[tmpd]
            # ***** 상어가 있는 곳은 이동 할 수 없음.******* x != 상어x and y != 상어y 아님!!
            if 0 <= nx < 4 and 0<= ny < 4 and not (nx,ny) in smell and (nx,ny) != (sharkx,sharky):
                new.append((nx,ny,tmpd))

                break
            else:# 반시계 방향으로 탐색
                tmpd -= 1
                if tmpd == -1:
                    tmpd = 7
        else:# 혹시 8방향 모두 이동 못한다면, 이동 안함. 자기꺼 append
            new.append((x,y,d))
    return new

def move_shark():
    t = []
    for arr in r:# 한 경로의 경우
        arr = list(arr)
        cnt = 0# 최적의 경로를 위해 몇 마리 물고기 제거 되는지 연
        nx = sharkx
        ny = sharky
        visited = [[0]*4 for _ in range(4)]


        for i in arr: # 상, 하 , 좌 ,우

            nx += sx[i]
            ny += sy[i]
            # **** 상어가 이동할 때, 다시 방문 했던 곳으로 갈 수 있기 때문에 제거된 물고기 수가 겹치지 않게
            # 한다.
            # 또한 복제가 되면서 상어와 물고기가 한 칸에 같이 존재할 수 있기 때문에, 상어가 있는 위치
            # 먼저 방문처리 하면 안됨.
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not visited[nx][ny]:
                    cnt += new_cnt[nx][ny]
                visited[nx][ny] = 1
            else:
                break

        else:
            arr.insert(0,cnt)
            t.append(arr)# 한 경로가 append됨



    t.sort(key = lambda x: (-x[0],x[1],x[2],x[3]))# 물고기 제거 개수, 상 좌 하 우 전순
    return t[0][1:] #경로반환.



while True:
    if time == s:
        break
    # 물고기 이동 후: 물고기 위치 배열 새로 할당, 물고기 각 칸에 몇 개인지 새로 할
    new_fish = move_fish()
    new_cnt = [[0]*4 for _ in range(4)]
    for x,y,d in new_fish:
        new_cnt[x][y] += 1


    # 상어 이동
    route = move_shark()# route 최적 경로 반환 [0,1,2]적
    for i in route:
        sharkx += sx[i]
        sharky += sy[i]
        if new_cnt[sharkx][sharky] != 0:# 혹시 그 칸에 물고기가 있으면 제거.
            new_cnt[sharkx][sharky] = 0
            smell[(sharkx,sharky)] = time # 어느 위치에 몇 번째의 냄새인지 남긴다.
    # 상어의 이동으로 제거된 물고기 개수와 위치 배열 update
    tmp = []
    for i,j,d in new_fish:#  상어이동 이후 물고기 제거 된 것 물고기 위치 배열에 반영.
        if new_cnt[i][j] == 0:
            continue
        tmp.append((i,j,d))
    new_fish = tmp
    #
    # 2 번전의 연습에서 남았던 물고기 냄새 제거

    for arr,nth in list(smell.items()):
        if nth == time - 2:
            del smell[(arr[0],arr[1])]

    # 복제 하기 : 물고기 위치 배열, 물고기 각 칸에 몇개 있는지 배열

    for x,y,d in new_fish:# 물고기 위치 배
        ori_fish.append((x,y,d))
    for i in range(4):# 물고기 각 칸에 몇개 있는지 update
        for j in range(4):
            ori_cnt[i][j] += new_cnt[i][j]
    # 연습 +1 완
    time += 1

answer = 0
for i in range(4):
    for j in range(4):
        answer += ori_cnt[i][j]

print(answer)