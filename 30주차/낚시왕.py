from collections import defaultdict
R,C,m = map(int,input().split())
board= [[[] for _ in range(C)] for _ in range(R)] # 각 r,c 칸에 [s,d,z]를 저장하는 격자판.
for _ in range(m):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = [s,d-1,z]

dx = [-1,1,0,0] # 상 하 우 좌 (1,2,3,4)
dy = [0,0,1,-1]

fisher = -1 # 현재 어부의 위치 
answer = 0 # 총 잡은 물고기의 크기.

def fisherMove(): # 어부가 1초 마다 오른쪽으로 이동.
    global fisher
    fisher += 1

def getShark(): # 가장 땅에 가까운, 즉 행이 작은 상어를 잡는다.
    global board,answer
    for x in range(R):
        if len(board[x][fisher]) > 0 :# 상어가 있다면
            answer += board[x][fisher][2] # 상어 크기 더해주기.
            board[x][fisher] = [] # 해당 칸 상어 제거.
            break

def sharkMove(): # 상어 이동. shark 라는 딕셔너리에 이동 후 각 좌표에 있는 상어의 s,d,z 배열 형태로 정보를 담는다. 
    shark = defaultdict(list)

    for x in range(R):
        for y in range(C):
            if len(board[x][y]) >0 :
                sp, dir, size = board[x][y] # 속도, 방향, 크기
                nx = x
                ny = y
                for _ in range(sp): # 속도(칸)만큼 1초 동안 이동
                    nx += dx[dir]
                    ny += dy[dir]
                    if 0 <= nx < R and 0 <= ny < C: 
                        continue
                    else: # 범위를 벗어나면 다시 반대방향으로 이동.
                        if dir % 2 == 0: # 0, 2일 때 (상, 우) => 하, 좌 반대로.
                            dir += 1
                        else:
                            dir -= 1
                        nx += (2*dx[dir])
                        ny += (2*dy[dir])
                shark[(nx,ny)].append((sp,dir,size)) # 이동 후 좌표를 shark에 넣기.
    return shark

def eatShark(shark): # 이동 후 상어의 정보를 새로운 격자판에 반영 & 한 칸에 두마리 이상 일때, 큰 상어 이외 다 제거.
    global board
    new = [[[] for _ in range(C)] for _ in range(R)]
    for x,y in shark:
        if len(shark[(x,y)]) == 1:
            sp, dir, size = shark[(x,y)][0]
            new[x][y] = [sp,dir,size]
        else: # 한 칸에 두마리 이상.
            arr = shark[(x,y)]
            arr.sort(key = lambda x : -x[2]) # 크기가 큰 상어가 나머지 잡아먹음.
            sp, dir, size = arr[0]
            new[x][y] = [sp,dir,size]
    board= new


if m != 0: # 상어가 1마리 이상일때.
    for _ in range(C):
        fisherMove() # 어부 이동
        getShark() # 상어 잡기
        change = sharkMove() # 상어 이동
        eatShark(change) # 이동 후 모습을 격자판에 반영, 한 칸에 여러마리 일 경우 제거.

print(answer)