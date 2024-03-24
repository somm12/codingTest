m,t = map(int,input().split())
px,py = map(int,input().split())
px -= 1
py -= 1
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
g = [[[] for _ in range(4)] for _ in range(4)]
dead = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(m):
    r,c,d = map(int,input().split())
    r -= 1
    c -=1
    d -=1
    g[r][c].append(d)

def inRange(x,y):
    return 0 <= x < 4 and 0 <= y < 4
def copyMonster():
    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for v in g[x][y]:
                tmp[x][y].append(v)
    return tmp

def moveMonster():# 몬스터 이동.
    global g
    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in g[x][y]:
                nx = x+dx[d]
                ny = y + dy[d]
                if not inRange(nx,ny) or (nx == px and ny == py) or len(dead[nx][ny]) > 0:# 조건에 해당한다면, 반시계 45도 회전하며 이동가능한 곳찾기.
                    nd = d
                    flag = True

                    for _ in range(8):
                        nd = (nd+1)%8
                        nx,ny = x+dx[nd],y+dy[nd]
                        if inRange(nx,ny) and [nx,ny] != [px,py] and len(dead[nx][ny]) == 0:
                            tmp[nx][ny].append(nd)
                            flag = False
                            break
                    if flag:# 이동 가능한 칸이 없다면 그대로.
                        tmp[x][y].append(d)
                else:
                    tmp[nx][ny].append(d)
    g= tmp

def movePM():# 팩맨 이동.
    global g,dead,px,py
    mx = [-1,0,1,0]# 상좌하우 우선순위.
    my =[0,-1,0,1]
    arr = []
    def dfs(res):
        if len(res)==3:
            arr.append(res)
            return
        for i in range(4):
            dfs(res+[i])
    dfs([])
    cand = []

    for a in arr:
        nx,ny = px,py
        cnt = 0
        visited = [[0]*4 for _ in range(4)]
        for di in a:
            nx += mx[di]
            ny += my[di]
            if not inRange(nx,ny):
                break
            if not visited[nx][ny]:# 잡아먹게 되는 몬스터 개수 세기. 개수 세는 것이 겹치지 않도록하기
                visited[nx][ny] = 1
                cnt += len(g[nx][ny])
        else:
            # 가능한 경우
            cand.append((cnt,a[0],a[1],a[2]))
    cand.sort(key = lambda x:-x[0])

    for di in cand[0][1:]:
        px += mx[di]
        py += my[di]
        if len(g[px][py]) > 0:# 몬스터가 죽는 그 칸에는 시체가 남음.
            dead[px][py].append(turn +2)
            g[px][py] = []

def removeDead():
    global dead
    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for v in dead[x][y]:
                if v <= turn:# dead[x][y] 번째 턴까지 시체가 남아 있기에. 시체 소멸.
                    continue

                else:
                    tmp[x][y].append(v)
    dead = tmp
def sumCopied():
    global g

    for x in range(4):
        for y in range(4):
            for v in copied[x][y]:
                g[x][y].append(v)


for turn in range(1,t+1):
    copied = copyMonster()

    moveMonster()
    movePM()
    removeDead()
    sumCopied()

answer = 0
for x in range(4):
    for y in range(4):
        answer += len(g[x][y])

print(answer)

