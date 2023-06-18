import copy
import sys
input = sys.stdin.readline
dx = [0,-1,-1,-1,0,1,1,1] # 물고기가 움직이는 8방향.
dy = [-1,-1,0,1,1,1,0,-1]

sdx = [-1,0,1,0] # 상어가 움직이는 상하좌우 방향.
sdy = [0,-1,0,1]

board = [[ [] for _ in range(4)] for _ in range(4)] # 물고기들의 위치정보를 저장할 3차원 배열.
smell = [[ [] for _ in range(4)] for _ in range(4)] # 물고기 냄새를 저장할 3차원 배열 (현재 연습 번호 담김).

m,s = map(int,input().split())

for _ in range(m):
    fx,fy,d = map(int,input().split())
    board[fx-1][fy-1].append(d-1) # x행 y열에 있는 물고기들의 위치를 담는다. 

sx,sy = map(int,input().split())
sx -=1 # 상어가 존재하는 위치.
sy -= 1
 
def copyFish(): # 물고기 복제마법에 적용 위함. 격자판을 복제한 것을 리턴. 
    temp = copy.deepcopy(board)
    return temp

def fishMove(): # 물고기들이 모두 이동. 이동 가능 방향 나올 때 까지 반시계 45도 회전.
    global board
    new = [[ [] for _ in range(4)] for _ in range(4)] # 물고기 이동 후 격자판을 보여주기 위함.
    for x in range(4):
        for y in range(4):
            if len(board[x][y]) > 0:
                for j in board[x][y]:
                    di = j
                    for _ in range(8):
                        nx = x + dx[di]
                        ny = y + dy[di]
                        if 0 <= nx < 4 and 0 <= ny < 4 and len(smell[nx][ny]) == 0 and (nx,ny) != (sx,sy):
                            new[nx][ny].append(di) # 이동 가능한 칸을 찾으면 break
                            break
                        di = (di-1)%8 # 반시계 방향으로 이동하기 위해 %8 하기.
                    else:
                        new[x][y].append(j) # 이동 가능한 방향이 없다면 그대로.
                    
    board = new 

def tryMove(arr): # arr 방향대로 상어가 3연속 이동할 때, 제외 되는 물고기 수 반환.
    cnt = 0
    nx = sx
    ny = sy
    visited = [[0]*4 for _ in range(4)]
    for i in arr:
        nx += sdx[i]
        ny += sdy[i]
        if 0 <= nx < 4 and 0<= ny < 4: # 범위 내로 벗어나면 해당 경우 제외.
            if not visited[nx][ny]:
                cnt += len(board[nx][ny])
            visited[nx][ny] = 1
        else:
            return -1 # -1 리턴하면 해당 경우는 제외됨.
    return cnt

def sharkMove(nth): # 이동방향을 선택 후, 해당 방향으로 3연속 상어가 이동.
    global board,sx,sy, cand

    cand.sort(key=lambda x : (-x[0],x[1])) # 제거된 물고기 개수가 많음 > 방향 사전순. 정렬
    arr = []
    
    for i in cand[0][1]:
        arr.append(int(i))
    
    for i in arr: 
        sx += sdx[i]
        sy += sdy[i]
        if len(board[sx][sy]) > 0: # 상어가 이동하면서 물고기가 제외 되고, 물고기 냄새가 남음.
            smell[sx][sy].append(nth) # 현재 연습 몇회차인지 할당. 나중에 냄새 제거할 때, 확인용.
            board[sx][sy] = [] # 물고기 제거.

def removeSmell(nth): # 2만큼 이전 연습에서 생긴 냄새를 제거.
    global smell
    for x in range(4):
        for y in range(4):
            tmp = []
            for v in smell[x][y]:# 두번 전 연습 때 생긴 냄새는 사라진다.
                if v == nth-2: 
                    continue
                else:
                    tmp.append(v)
            smell[x][y] = tmp

def copyMagic(): # 복제되었던 물고기를 다시 반영.
    global board
    for x in range(4):
        for y in range(4):
            for v in prevBoard[x][y]:
                board[x][y].append(v)

def sharkDFS(L,arr): # 4*4*4 3연속 이동가능한 모든 경우를 찾는 함수.
    global cand
    if L == 3:
        removedF = tryMove(arr) # 해당 방향으로 이동 후, 제외 되는 물고기 수와 방향 형태 append.
        tmp = ''
        for i in arr:
            tmp += str(i)
        if removedF != -1:
            cand.append((removedF, tmp))
        return
    
    for i in [0,1,2,3]:
        sharkDFS(L+1, arr+[i])

for nth in range(1,s+1): # s번 마법 연습.
    
    prevBoard = copyFish() # 물고기 복제
    fishMove() # 물고기들 이동.
    
    cand = [] # 상어가 이동 가능한 모든 경우가 되는 후보를 담을 배열 (제외 되는 물고기수, '000':방향)
    sharkDFS(0,[]) # 상어가 이동 가능한 모든 경우 찾기.

    sharkMove(nth) # 상어 이동.
    
    
    removeSmell(nth) # 2번 이전 연습 때 물고기 냄새 제거

    copyMagic() # 복제된 물고기 반영.
    



answer = 0 # 총 남은 물고기 수 구하기
for x in range(4):
    for y in range(4):
        answer += len(board[x][y])
print(answer)

