n,m,x,y,k = map(int,input().split())
board=  []
for _ in range(n):
    board.append(list(map(int,input().split())))
command = list(map(int,input().split()))
dice = [0]*6
dx = [0,0,-1,1] # 동서북남
dy = [1,-1,0,0]

def moveDice(direction): # 주사위 움직이기.
    global dice, x,y,board
    nx = x + dx[direction] # 해당 방향으로 움직였을 때.
    ny = y + dy[direction]
    a,b,c,d,e,f = dice # 현재 주사위의 전개도.

    if 0 <= nx < n and 0 <= ny < m: # 지도 바깥이 아니라면,
        if direction == 0: # 동쪽일 때
            dice = [d,b,a,f,e,c]
        elif direction ==1: # 서쪽일 때
            dice = [c,b,f,a,e,d]
        elif direction == 2:# 북쪽일 때
            dice= [e,a,c,d,f,b]
        else:# 남쪽 일때
            dice = [b,f,c,d,a,e]
        
        if board[nx][ny] == 0: # 움직인 칸이 0 이면, 바닥면 수가 칸으로 복사됨.
            board[nx][ny] = dice[5]
        else:                   # 움직인 칸이 0 아니면, 칸에서 바닥면으로 수가 복사됨. 해당 칸은 0이 된다.
            dice[5] = board[nx][ny]
            board[nx][ny] = 0
        x,y = nx,ny # 현재 주사위 좌표도 update시킴.
        return True
    return False # 지도 밖으로 이동은 무시.

for direction in command:
    direction -= 1 # 입력이 1,2,3,4 중 하나 이므로, 인덱스 맞추기 위함.
    if moveDice(direction): # 지도 범위 내 이동이라면, 윗면 출력.
        print(dice[0])
# 1. 지도 범위 내 이동 가능한지 체크
# 2. 주사위 위치가 바뀌고, 전개도 변경.
# 3. 칸에서 바닥면, 바닥면에서 칸 으로 칸이 0일 때 또는 아닐 때에 따라 변경됨.
# 4. 윗면 출력.