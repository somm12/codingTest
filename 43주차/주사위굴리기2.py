from collections import deque

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0
nowD = 0# 현재 바로보고 있는 방향.
dx = [0,1,0,-1]# 동남서북.
dy = [1,0,-1,0]
sx,sy = 0,0 #주사위 위치
dice = [1,2,3,4,5,6]# 주사위 전개도를 담는 배열.

def move():# 주사위 이동.
    global nowD, sx,sy, dice
    nx = sx+dx[nowD]
    ny = sy+dy[nowD]
    if not( 0<=nx < n and 0 <= ny <m):# 범위 밖이면 반대 방향으로 바꿔서 이동.
        nowD = (nowD+2)%4
        sx += dx[nowD]
        sy += dy[nowD]
    else:
        sx,sy = nx,ny
    a,b,c,d,e,f = dice# 주사위 전개도 바꾸기.
    if nowD == 0:#동쪽일때
        dice=[d,b,a,f,e,c]
    elif nowD == 1:#남쪽
        dice= [b,f,c,d,a,e]
    elif nowD == 2:#서쪽
        dice = [c,b,f,a,e,d]
    else:#북쪽
        dice = [e,a,c,d,f,b]

def getScore():# 점수 획득. 동서남북 연속으로 같은 숫자로 갈 수 있는 칸 수 구하기 * 칸에 들은 값.
    global answer
    value = g[sx][sy]
    x,y,=sx,sy
    q = deque()
    q.append((x,y))
    arr = {}
    visited = [[0]*m for _ in range(n)]
    visited[sx][sy] = 1
    while q:
        x,y = q.popleft()
        arr[(x,y)] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == value and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
    answer += (len(arr)*value)
def direction():# 아랫면 숫자 vs 칸에 적힌 수 비교 후, 바꿀 방향 정하기.
    global nowD
    A = dice[-1]
    B = g[sx][sy]
    if A > B:# 아랫면이 크면 시계 90도 회전.
        nowD = (nowD+1)%4
    elif A < B:# 칸에 적힌 수가 크면 반시계 90도 회전.
        nowD = (nowD-1)%4


for _ in range(k):
    move()
    getScore()
    direction()
print(answer)
# 삼성 기출.