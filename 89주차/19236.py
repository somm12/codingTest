import copy
board = [[]*4 for _ in range(4)]
answer = 0
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    a = list(map(int,input().split()))
    for j in range(4):
        board[i].append([a[2*j], a[2*j + 1]-1])
def isFishExist(board,num):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == num:
                return (x,y)
def fishMove(sx,sy,board):
    for i in range(1,17):
        pos = isFishExist(board,i)
        if pos:
            x,y = pos
            d = board[x][y][1]
            nx = x
            ny = y
            for _ in range(8):
                nx = x+ dx[d]
                ny = y + dy[d]
                if 0 <= nx < 4 and 0 <= ny < 4 and [nx,ny] != [sx,sy]:
                    tox,toy = board[nx][ny]
                    board[nx][ny] = [i,d]
                    board[x][y] = [tox,toy]
                    break
                d += 1
                d %= 8

def sharkMove(sx,sy,board):
    arr = []
    d = board[sx][sy][1]
    nx = sx
    ny = sy
    for _ in range(3):
        nx += dx[d]
        ny += dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] != -1:
            arr.append((nx,ny))
    return arr
   

def dfs(sx,sy,eat,board):
    global answer
    # 해당 위치로 상어 좌표 바뀜. 물고기 먹기, 물고기 사라짐.
    new = copy.deepcopy(board)
    eat += new[sx][sy][0]
    new[sx][sy][0] = -1
    # 물고기 이동.
    fishMove(sx,sy,new)
    # 상어이동. 더 이상 이동할 위치가 없다면 종료.
    arr = sharkMove(sx,sy,new)
    if len(arr) == 0:
        answer = max(answer,eat)
        return
    for x,y in arr:
        dfs(x,y,eat,new)
dfs(0,0,0,board)
print(answer)
# 백준 청소년 상어.