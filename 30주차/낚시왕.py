from collections import defaultdict
import sys
input = sys.stdin.readline
R,C,m = map(int,input().split())
board= [[[] for _ in range(C)] for _ in range(R)] # 각 r,c 칸에 [s,d,z]를 저장하는 격자판.
for _ in range(m):
    r,c,s,d,z = map(int,input().split())
    d -=1
    if d <= 1: # 상 하 => 한 싸이클 RorC -1 *2 로 나누면 더 적은 칸으로 speed 만들 수 있음.
        s %= (R -1) * 2; 
    elif d<= 3:# 우 좌
        s %= (C -1) * 2;
    board[r-1][c-1] = [s,d,z]

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
            if len(board[x][y]) > 0 :
                sp, dir, size = board[x][y] # 속도, 방향, 크기
                row, col = x,y
                speed = sp
                while True: 
                    ny = col + sp*dy[dir]
                    nx = row + sp*dx[dir]
                    if 0 <=nx < R and 0<= ny < C: # 이동 후, 범위 이내면 break
                        break
                    if dir <= 1:# 상하. 
                        if nx < 0: # -라면 위쪽 방향이었을 것. 속력을 x좌표만큼 줄이고, 좌표를 다시 0으로 시작.
                            sp -= row
                            row = 0
                        else: # 범위를 벗어났으면, 아래쪽 방향이었을 것. 맨아래쪽까지의 거리를 속력에서 빼고, 좌표를 다시 우측 마지막 부터 시작.
                            sp -= R-1 -row
                            row = R-1
                    else: # 좌우. 상하일 때와 동일.
                        if ny < 0:
                            sp -= col
                            col = 0
                        else:
                            sp -= C-1-col
                            col = C-1
                    dir ^= 1 # 방향이 바뀌었으니 xor연산 이용. 0 => 1, 1 => 0, 2=> 3, 3=>2
            
                shark[(nx,ny)].append((speed,dir,size)) # 이동 후 좌표를 shark에 넣기.
    
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
    for nth in range(C):
        
        fisherMove() # 어부 이동
        getShark() # 상어 잡기
        change = sharkMove() # 상어 이동
        eatShark(change) # 이동 후 모습을 격자판에 반영, 한 칸에 여러마리 일 경우 제거.

print(answer)

# 물고기 이동시에만 100*100*1000(최대 속력) => 천만이므로, 전체 100번 이동하면 10억이 걸림.
# 시간 초과 방지를 위해, 빠르게 이동할 수 있는 방법이 필요.
# speed를 총 가능한 사이클 수로 나눈 나머지만큼 이동하도록 줄이고,
# 벽에 다다르면 방향을 바꾸고 좌표를 찾아나갈 수 있는 방법으로 구하기.

# 방향이 좌측을 바라보고 5만큼 이동시, 열위치는 인덱스로 1일때. => 결과적으로 방향은 반대방향. 인덱스 4.
# 좌측으로 쭉 이동 후, - 부호가 나오면, 먼저 맨 좌측 으로 이동 시키고, 그 만큼 이동 할 속력을 빼주고 다시 반대방향으로 나머지
# 속력 만큼 이동시키는 방법. 만약 우측방향으로 범위가 넘어가면, 맨 우측으로 일단 이동 시키고(마지막 인덱스 - 현재위치 만큼 이동 후),
# 맨 우측 좌표에서 다시 좌측으로 이동할 준비. 등.