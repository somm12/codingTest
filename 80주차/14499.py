n,m,x,y,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

command = list(map(int,input().split()))
dice = [0]*6
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < m

for di in command:
    di -= 1
    x +=dx[di]
    y += dy[di]
    if not inRange(x,y):
        x -= dx[di]
        y -= dy[di]
        continue
    # 주사위 변경.
    a,b,c,d,e,f = dice
    if di == 0:#동
        dice = [d,b,a,f,e,c]
    elif di == 1:#서
        dice =[c,b,f,a,e,d]
    elif di == 2:#북
        dice = [e,a,c,d,f,b]
    else:# 남
        dice = [b,f,c,d,a,e]
    # 칸, 주사위 바닥면 값 복사.
    if g[x][y] == 0:
        g[x][y] = dice[-1]
    else:
        dice[-1] = g[x][y]
        g[x][y] = 0
    print(dice[0])
# 주사위 굴리기