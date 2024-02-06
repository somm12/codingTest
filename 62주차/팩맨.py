mx = [-1,-1,0,1,1,1,0,-1]
my = [0,-1,-1,-1,0,1,1,1]# 몬스터의 방향. 반시계 방향대로.
px = [-1,0,1,0]
py = [0,-1,0,1]# 팩맨 방향 => 우선순위 대로. 상 좌 하 우


m,t = map(int,input().split())
pmx,pmy = map(int,input().split())

pmx -= 1
pmy -= 1

g = [[[] for _ in range(4)] for _ in range(4)]
dead = [[[] for _ in range(4)] for _ in range(4)]

for i in range(1,m+1):
    r,c,d = map(int,input().split())
    g[r-1][c-1].append(d-1)
pmDirection = []# 팩맨이 이동할 수 있는 방향의 모든 경우 상>좌>하>우 우선순위
# ex) [0,0,0], [,,]

def inRange(x,y):
    return 0 <= x < 4 and 0 <= y < 4

def init():# 팩맨 이동 방향 모든 경우의 수 셋팅
    def dfs(res):
        if len(res) == 3:
            pmDirection.append(res)
            return
        for i in range(4):
            dfs(res+[i])
    dfs([])

def copying():# 복제.
    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            arr = g[x][y][:]
            tmp[x][y]= arr
    return tmp

def mMove():# 몬스터 이동.
    global g
    tmp = [[[] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for d in g[x][y]:
                nx,ny = x+mx[d], y+my[d]
                # 격자밖 or 시체 있음 or 팩맨 있음 => 반시계 45도 방향씩 보면서 가능한 칸 찾기.
                if not inRange(nx,ny) or len(dead[nx][ny]) > 0 or [nx,ny] == [pmx,pmy]:
                    di = d
                    for _ in range(8):
                        di = (di+1)%8
                        nx,ny = x+mx[di],y+my[di]
                        if inRange(nx,ny) and len(dead[nx][ny]) == 0 and [nx,ny] != [pmx,pmy]:
                            tmp[nx][ny].append(di)
                            break
                    else:# 이동 가능한 위치가 없다면 그대로.
                        tmp[x][y].append(d)
                else:# 바로 이동 가능!
                    tmp[nx][ny].append(d)
    g = tmp# 위치 변경된거로 업데이트.

def pmMove():# 팩맨 이동.
    global pmx,pmy,g
    cand = []
    for arr in pmDirection:# 연속 3칸 이동 중, 하나의 경우인 arr
        tx,ty = pmx,pmy
        cnt = 0
        visited = [[0]*4 for _ in range(4)]# 개수를 세기 위한 방문 배열.
        for d in arr:
            tx += px[d]
            ty += py[d]
            if not inRange(tx,ty):#격자 밖으로 가는 경우는 고려하지 않음
                break
            
            if not visited[tx][ty]:# 방문 하지 않은 칸이라면 cnt에 개수 포함.
                cnt += len(g[tx][ty])
                visited[tx][ty] = 1
        else:# 모두 격자 안으로 왔다면!
            cand.append([cnt] + arr)
    cand.sort(key = lambda x:(-x[0],x[1],x[2],x[3]))# 죽는 몬스터 개수가 많고, 그 다음으로 상 좌 하우 우선순위.
    for d in cand[0][1:4]:
        pmx += px[d]
        pmy += py[d]
        if len(g[pmx][pmy]) > 0:# 해당칸에 몬스터가 죽었다면, 죽음 처리 + 시체 표시.
            dead[pmx][pmy].append(turn +2)# 시체는 턴 2번 동안 유지.
            g[pmx][pmy] = []
        
        

def deadRemove():#시체 제거
    global dead
    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for v in dead[x][y]:
                if v > turn:# 현재의 턴보다 유지되는 값이 크다면 그대로 유지.
                    tmp[x][y].append(v)
    dead = tmp

def addCopied():# 복제된거 다시 넣기.
    global g
    for x in range(4):
        for y in range(4):
            for v in copied[x][y]:
                g[x][y].append(v)


init()

for turn in range(1,t+1):
    copied = copying()
    
    mMove()
  
    pmMove()

    deadRemove()
 
    addCopied()

answer = 0# 살아남은 몬스터 개수 세기.
for x in range(4):
    for y in range(4):
        answer += len(g[x][y])
print(answer)
