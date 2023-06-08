import copy # deepcopy 사용해서 재귀 호출에서 참조를 막기 위함.
board = [[]*4 for _ in range(4)]
answer = 0
# 8가지 방향. -> 방향갈 수 록 반시계.
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    a = list(map(int,input().split()))
    for j in range(4):
        board[i].append([a[2*j], a[2*j + 1]-1])
# 해당 번호를 가진 물고기가 존재하는지 확인하고 존재하면 x,y 위치를 반환.
def isFishExist(board,num):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == num:
                return (x,y)
# 물고기가 낮은 번호 순서로 움직인다.
def fishMove(sx,sy,board):
    for i in range(1,17):
        pos = isFishExist(board,i)
        if pos: # i번 물고기가 존재한다면,
            x,y = pos
            d = board[x][y][1] # 물고기가 가진 방향.
            nx = x
            ny = y
            for _ in range(8): # 반시계 방향으로 이동 할 수 있는 칸 만날때 까지 반복.
                nx = x+ dx[d]
                ny = y + dy[d]
                if 0 <= nx < 4 and 0 <= ny < 4 and [nx,ny] != [sx,sy]:
                    tox,toy = board[nx][ny]
                    board[nx][ny] = [i,d] # 현재 물고기 이동. [현재 물고기 번호, 현재 가리키는 방향]
                    board[x][y] = [tox,toy] # 원래 있던 자리 물고기는 x,y로 이동.
                    break # 이동 했으니 break
                d += 1
                d %= 8 # index out of range 막기.

def sharkMove(sx,sy,board): # 상어 이동. 이동 가능한 칸 위치 배열 반환.
    arr = []
    d = board[sx][sy][1] # 상어의 위치.
    nx = sx
    ny = sy
    for _ in range(3): # 최대 3칸 이동(4x4 이기 때문.)
        nx += dx[d]
        ny += dy[d]
        # 범위 내, 물고기가 있는 칸만 이동 가능.
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] != -1: 
            arr.append((nx,ny))
    return arr
   
 # 상어가 선택한 이동 칸 들의 모든 경우를 완전 탐색하여, 먹은 물고기 번호 합 구하기.
def dfs(sx,sy,eat,board): # 상어의 위치와, 현재까지의 먹은 번호 합, 현재까지 board 상태.
    global answer
    new = copy.deepcopy(board) # deepcopy 사용으로 참조가 발생 막기
    eat += new[sx][sy][0] # 물고기 번호 더하기
    new[sx][sy][0] = -1 # 물고기가 제거 표시로 번호 부분에 -1 할당.

    fishMove(sx,sy,new) # 물고기 이동
    
    arr = sharkMove(sx,sy,new) # 상어이동
    if len(arr) == 0: # 상어가 더이상 이동X 상태가 된다면, eat 업데이트 및 재귀 호출 종료.
        answer = max(answer,eat)
        return
    for x,y in arr: # 상어가 이동 가능한 좌표를 반환하고 해당 위치로 상어가 이동.
        dfs(x,y,eat,new)
dfs(0,0,0,board) # 처음에 상어가 0,0으로 이동한다.
print(answer)