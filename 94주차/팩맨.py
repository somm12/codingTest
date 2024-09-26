dx = [-1,-1,0,1,1,1,0,-1]# 몬스터 이동 방향. 인덱스가 커질 수록 반시계 방향.
dy= [0,-1,-1,-1,0,1,1,1]

pdx =[-1,0,1,0]# 팩맨 이동 방향 상 좌 하 우
pdy = [0,-1,0,1]

dead = [[[] for _ in range(4)] for _ in range(4)]
m,t = map(int,input().split())

px,py = map(int,input().split())
px -= 1
py -= 1
g = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    r,c,d = map(int,input().split())
    g[r-1][c-1].append(d-1)
arr = []
def dfs(res):# 가질 수 있는 이동 경로 64가지 구하기.
    if len(res) == 3:
        arr.append(res)
        return
    for i in range(4):
        dfs(res+[i])
dfs([])


def inRange(x,y):
    return 0 <=x < 4 and 0 <= y < 4

def copyM():# 몬스터 복제해두기 

    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for di in g[x][y]:
                tmp[x][y].append(di)
    return tmp

def mMove():# 몬스터 이동.
    global g
    tmp = [[[] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for di in g[x][y]:
                nd = di
                for _ in range(8):
                    nx = x+ dx[nd]
                    ny = y + dy[nd]
                    if not inRange(nx,ny) or len(dead[nx][ny]) > 0 or [nx,ny] == [px,py]:# 범위밖, 시체 존재, 팩맨 위치 피하기.
                        nd = (nd+1)%8 # 45씩 반시계방향으로 확인.
                    else:# 가능하면 이동.
                        tmp[nx][ny].append(nd)
                        break
                else:# 이동 못하면 그대로.

                    tmp[x][y].append(di)#그대로
    g= tmp
def pMove():# 팩맨 이동.
    global g,px,py,dead
    cand =[]
    for a in arr:
        cnt = 0
        flag= True
        nx,ny = px,py
        s = set()# 이미 방문했던 위치 저장. 잡아먹을 수 있는 몬스터 개수 셀 때 중복 방지.
        for di in a:
            nx += pdx[di]
            ny += pdy[di]
            if not inRange(nx,ny):
                flag= False
                break
            elif (nx,ny) not in s:
                s.add((nx,ny))
                cnt += len(g[nx][ny])
        if flag:
            cand.append((cnt,a))

    cand.sort(key=lambda x: -x[0])# 가장 많은 순.
    nArr = cand[0][1]
    nx,ny = px,py
    for di in nArr:
        nx += pdx[di]
        ny += pdy[di]
        if len(g[nx][ny]) > 0:# 몬스터가 존재하면, 삭제되고 그 자리에 시체 남김(2턴 동안 유지)
            g[nx][ny] = []
            dead[nx][ny].append(nth+2)

    px,py = nx,ny

def deleteDead():# 시체 유효기간이 2턴이 아직 안되면. 남기기.
    global  dead
    for x in range(4):
        for y in range(4):
            tmp = []
            for v in dead[x][y]:
                if v > nth:
                    tmp.append(v)
            dead[x][y] = tmp[:]

def pasteM():# 복제된거 붙여넣기.
    global  g
    for x in range(4):
        for y in range(4):
            for v in copied[x][y]:
                g[x][y].append(v)


for nth in range(1,t+1):
    copied = copyM()
    mMove()

    pMove()
    deleteDead()
    pasteM()


answer = 0
for x in range(4):
    for y in range(4):
        answer += len(g[x][y])
print(answer)
# 코드트리 문제.