n,m,x,y,k = map(int,input().split())
board = []
dice = [0]*6
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(n):
    board.append(list(map(int,input().split())))
command = list(map(int,input().split()))

def move(x):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if x == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
    elif x== 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = c,b,f,a,e,d
    elif x == 3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = e,a,c,d,f,b
    else:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = b,f,c,d,a,e

for i in command:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    if nx < 0 or nx >= n or ny < 0 or ny >=m:
        continue
    x = nx
    y = ny
    move(i)
    if board[nx][ny] != 0:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
    else:
        board[nx][ny] = dice[-1]
    print(dice[0])