m,t = map(int,input().split())
px,py = map(int,input().split())
px -= 1
py -= 1

dead = [[ [] for _ in range(4)] for _ in range(4)]
g = [[ [] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    r,c,d =map(int,input().split())
    g[r-1][c-1].append(d-1)

direction = []# 팩맨이 이동할 수 있는 총 경우 64가지.
dx = [-1,-1,0,1,1,1,0,-1] # 위쪽 방향부터 반시계 방향 8방향.
dy = [0,-1,-1,-1,0,1,1,1]
sx = [-1,0,1,0] # 상 좌 하 우. => 팩맨이 이동할 방향 4가지.
sy = [0,-1,0,1]

def dfs(res):# 팩맨이 이동할 수 있는 모든 가지수 64가지를 구할 함수.
    global direction
    if len(res) == 3:
        direction.append(res)
        return
    for v in [0,1,2,3]:
        dfs(res+[v])

dfs([])

def copyMonster():# 현재 물고기 상태 배열 g 복사하기.
    arr =[[ [] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            arr[i][j] = g[i][j]
  
    return arr
def moveMonster():# 몬스터 이동.
    global g
    tmp = [[ [] for _ in range(4)] for _ in range(4)]# 이동 후 상태를 담을 배열.
    for x in range(4):
        for y in range(4):
            for d in g[x][y]:
                di = d
                for _ in range(8):# 반시계45도 씩 회전하여 이동 가능한 칸 찾기.
                    nx = x+dx[di]
                    ny = y+dy[di]
                    # 격자 내, 팩맨이 없고, 시체가 없는 칸.
                    if 0 <= nx < 4 and 0 <= ny < 4 and [px,py]!= [nx,ny] and len(dead[nx][ny]) == 0:
                        tmp[nx][ny].append(di)
                        break
                    di = (di+1)%8
                else:# 8방향 모두 이동 불가하다면, 그대로.
                    tmp[x][y].append(d)
    g= tmp

def realMove(arr):# arr 방향대로 팩맨이 움직임.
    global px,py,g,dead
    visited = [[0]*4 for _ in range(4)]
    for d in arr:
        px += sx[d]
        py += sy[d]
        if not visited[px][py]:
            visited[px][py]=1
            if len(g[px][py]):# 경로 중에 몬스터가 있다면 잡아먹고, 해당 자리에는 시체 표시(2개 턴동안 유지.)
                g[px][py] = []
                dead[px][py].append(turn+2)
def removeDead():# 시체 소멸
    global dead
    newD = [[ [] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for v in dead[x][y]:
                if turn != v:# 현재의 턴과 같은 시체라면 소멸.
                    newD[x][y].append(v)
    dead = newD

def addCopy():# 복사해두었던 배열과 g를 다시 합침.
    global g
    for x in range(4):
        for y in range(4):
            for d in copied[x][y]:
                g[x][y].append(d)
def packManMove():# 팩맨 이동
    global px,py,g,dead
    cand = []# 총 이동 가능한 경로를 담을 후보 배열.
    for arr in direction:# 이동 경우 64가지 중에서.
        nx,ny = px,py # 가장 몬스터를 많이 죽일 수 있으며, 상, 좌 , 하, 우 순서인 경우를 선택.
        cnt = 0
        visited = [[0]*4 for _ in range(4)]# 방문처리를 통해서 이미 방문했던 칸의 몬스터 개수를 중첩되어서 계산되지 않도록 한다.
        for d in arr:
            nx += sx[d]
            ny += sy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += len(g[nx][ny])
            else:# 격자를 벗어나면 이동 경로로 포함할 수 없다.
                break
        else:
            cand.append(([cnt]+arr))
    
    cand.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))# 가장 많이 몬스터가 죽으면서, 상 좌 하 우(0,1,2,3) 순으로 선택.=> 즉, 숫자가 작은순.
  
    tmp = cand[0][1:]# 이동할 방향 구하기
    realMove(tmp)# 해당 방향으로 이동 시킴.



for turn in range(1,t+1):
    copied = copyMonster()# 복사해두기
    moveMonster()# 몬스터 이동
    packManMove()# 팩맨 이동
    removeDead()# 시체 소멸
    addCopy()# 복사한 몬스터 반영.
answer = 0
for x in range(4):
    for y in range(4):
        answer += len(g[x][y])# 총 남은 몬스터 개수 구하기.
print(answer)
# 삼성 기출문제.