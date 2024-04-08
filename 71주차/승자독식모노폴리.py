n,m,k = map(int,input().split())
g = [ [ [] for _ in range(n)] for _ in range(n)]# 플레이어 번호를 담는 배열.
player = {}
scope = [ [ [] for _ in range(n)] for _ in range(n)]# 땅의 주인과, 그 유효기간. 
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j] > 0:
            g[i][j].append(arr[j])
            scope[i][j] = [arr[j],k]
            player[arr[j]] = [i,j]
dx = [-1,1,0,0]# 상 하 좌우
dy = [0,0,-1,1]

direct = {}
for i,v in enumerate(list(map(int,input().split()))):
    player[i+1].append(v-1)

for num in range(1,m+1):
    direct[num] = []
    for _ in range(4):
        a,b,c,d = map(int,input().split())
        direct[num].append([a-1,b-1,c-1,d-1])

time = 0

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def check():# 계약 기간 1씩 줄이기.
    global scope

    for x in range(n):
        for y in range(n):
            if len(scope[x][y]) > 0:
                scope[x][y][1] -= 1
                if scope[x][y][1] == 0:# 기간이 0 이면 빈 배열로 비우기.
                    scope[x][y] = []

def move():
    global player,scope,g
    tmp = {}# 이동 이후 플레이어 위치와 방향 상태.
    newG = [ [ [] for _ in range(n)] for _ in range(n)]# 이동이후의 격자 상태.
    for num in player:
        x,y,d= player[num]
        emp = []# 아무와도 계약하지 않았을 경우, 다음위치와 방향
        mine = []# 자신이 독점한 경우일 때, 다음 위치와 뱡향.
        for i in direct[num][d]:
            nx = x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny):
                if len(scope[nx][ny]) == 0:
                    emp.append((nx,ny,i))
                    break
                elif scope[nx][ny][0] == num:
                    mine.append((nx,ny,i))
        if len(emp) > 0:
            tmp[num] = emp[0]
            nx,ny,nd = emp[0]
            newG[nx][ny].append(num)

        else:
            tmp[num] = mine[0]
            nx,ny,nd = mine[0]
            newG[nx][ny].append(num)

        
    player = tmp
    g = newG

def remove():# 한 칸에 여러명이면 작은 번호 빼고 삭제.
    global g,player,scope
    tmp = {}
    for x in range(n):
        for y in range(n):
            if len(g[x][y]) > 1:
                g[x][y].sort()
                number= g[x][y][0]
                g[x][y] = [number]
                tmp[number] = player[number]
            elif len(g[x][y]) == 1:
                number = g[x][y][0]
                tmp[number] = player[number]


    player = tmp

def contract():# 이동 후에 독점 계약 실시.
    global scope

    for num in player:
        x,y,_ = player[num]
        scope[x][y] = [num,k]


def isFinish():# 1번만 살아 남았는지 확인.
    return len(player) == 1 and 1 in player

while time < 1000:

    move()# 이동
    remove()# 한 칸에 두명이면 처리
    check()# 턴이 한번 끝나고, 계약기간 -1.
    contract()# 이번 턴에서 이동한 칸에서 새로운 계약 맺기.

    time += 1

    if isFinish():
        break
   
if time >= 1000:# 턴이 1000이상 걸린다면, -1.
    print(-1)
else:
    print(time)