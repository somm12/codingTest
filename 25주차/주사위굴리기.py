n,m,x,y,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dice = [0]*6
track = list(map(int,input().split()))

def move(s):# 이동 방향쪽으로 주사위 전개도를 바꾸기
    global dice, x, y
    dx = [0,0,0,-1,1]#동서북남
    dy = [0,1,-1,0,0]
    nx = x + dx[s]
    ny = y + dy[s]
    # 지도 밖으로 이동하는 명령은 무시.
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return False
    # 지도 범위 내로 이동 가능하면 주사위 위치 변경.
    x = nx
    y = ny
    a,b,c,d,e,f = dice
    if s == 1: # 동쪽 방향으로 이동
        a,b,c,d,e,f = d,b,a,f,e,c
    elif s == 2: # 서쪽으로 이동
        a,b,c,d,e,f = c,b,f,a,e,d
    elif s == 3: # 북으로 이동
        a,b,c,d,e,f = e,a,c,d,f,b
    else: # 남으로 이동
        a,b,c,d,e,f = b,f,c,d,a,e
    dice = [a,b,c,d,e,f] # 주사위 전개도 업데이트
    return True

def copy():
    global g,dice
    if g[x][y] == 0:
        g[x][y] = dice[5]
    else:
        dice[5] = g[x][y]
        g[x][y] = 0

for d in track:# 각 방향으로 이동하기
    if move(d): # 지도 안쪽으로 이동 가능하다면 명령어 시행.
        copy() # 이동한 칸이 0 이면  아랫면 칸에 복사, 아니면 주사위 아랫면으로 칸 내용 복사 후 해당 칸은 0.
        print(dice[0]) # 주사위 윗면 출력.