n,m,x,y,k =map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

arr = list(map(int,input().split()))

dice = [0]*6

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def inRange(x,y):
    return 0 <= x< n and 0 <=y < m

for i in range(k):
    a,b,c,d,e,f = dice
    di = arr[i] - 1
    nx,ny= x+dx[di],y+dy[di]
    if not inRange(nx,ny): continue# 지도를 벗어나는 것은 무시.

    x,y=nx,ny# 방향으로 이동.
    if di == 0:# 동
        dice = [d,b,a,f,e,c]
    elif di == 1:# 서
        dice = [c,b,f,a,e,d]
    elif di == 2:#북
        dice = [e,a,c,d,f,b]
    else:#남
        dice= [b,f,c,d,a,e]

    # 칸이 0이면 주사위 아랫면 수를 칸으로 복사.
    if g[x][y] == 0:
        g[x][y] = dice[-1]
    else:#아니면 해당 숫자를 주사위 아랫면으로 복사, 해당 칸은 0.
        dice[-1] = g[x][y]
        g[x][y] = 0
    print(dice[0])# 윗면(상단) 숫자 출력.
# 백준 주사위 굴리기.
