from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0
di = 0
dice = [1,2,3,4,5,6]
dicex,dicey = 0,0

def move():# 방향대로 한 칸 이동. 주사위 전개도 변경.
    global dicex,dicey,dice
    dicex,dicey = dicex+dx[di], dicey+dy[di]

    a,b,c,d,e,f = dice
    if di == 0:
        dice = [d,b,a,f,e,c]
    elif di == 1:
        dice = [e,a,c,d,f,b]
    elif di == 2:
        dice = [c,b,f,a,e,d]
    else:
        dice = [b,f,c,d,a,e]

def inRange(x,y):
    return 0 <=x < n and 0 <= y < n
def getScore():# 인접한 칸 중, 주사위 해당 칸 값과 같은 것 만큼 점수 획득.
    global answer

    q = deque()
    q.append((dicex,dicey))
    visited = [[0]*n for _ in range(n)]
    visited[dicex][dicey] = 1
    value = g[dicex][dicey]
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == value:
                visited[nx][ny] = 1
                q.append((nx,ny))
    answer += (cnt * value)

def changeDirection():# 주사위 바닥면과 주사위 해당칸 값 비교
    global di

    bottom = dice[-1]
    if bottom > g[dicex][dicey]:
        di = (di+1)%4
    elif bottom < g[dicex][dicey]:
        di = (di-1)%4
    nx,ny = dicex+ dx[di], dicey + dy[di]

    if not inRange(nx,ny):
        di = (di+2) % 4

for nth in range(1,m+1):
    move()
    getScore()
    changeDirection()
print(answer)