from collections import deque
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dice = [1,2,3,4,5,6]

diceX,diceY = 0,0
di = 1
answer = 0
dx = [-1,0,1,0] # 상 우 하 좌
dy = [0,1,0,-1]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def getPoint(value):
    global answer
    q = deque()
    q.append((diceX,diceY))
    visited = [[0]*n for _ in range(n)]
    visited[diceX][diceY] = 1
    total = 0
    while q:
        x,y = q.popleft()
        total += g[x][y]
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == value:
                visited[nx][ny] = 1
                q.append((nx,ny))
    answer += total

def diceChange():
    global dice
    a,b,c,d,e,f = dice
    if di == 0:#상
        dice = [b,f,c,d,a,e]
    elif di == 1:# 우
        dice = [d,b,a,f,e,c]
    elif di == 2:#하
        dice = [e,a,c,d,f,b]
    else:#좌
        dice = [c,b,f,a,e,d]
def directChange():
    global di
    bottom = dice[-1]
    board = g[diceX][diceY]
    if bottom > board:
        di = (di+1)%4
    elif bottom < board:
        di = (di-1)%4
    nx,ny = diceX + dx[di], diceY + dy[di]

    if not inRange(nx,ny):
        di = (di+2)%4

for _ in range(m):
    diceX += dx[di]# 다음 위치로 이동.
    diceY += dy[di]
    
    target = g[diceX][diceY]# 주사위가 올려진 칸의 격자판 숫자
    
    getPoint(target)# 해당 숫자와 인접하게 같은 숫자들의 합을 점수로 획득.
    diceChange()# 움직였던 방향대로 주사위 상태 변경.
    directChange()# 다음에 이동할 방향 선정.
print(answer)