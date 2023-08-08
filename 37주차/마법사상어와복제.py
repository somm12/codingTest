import copy
sdx = [-1,0,1,0]

sdy = [0,-1,0,1]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

m,s = map(int,input().split())
fish = [[ [] for _ in range(4)] for _ in range(4)]
smell = [[ [] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    fx,fy,d= map(int,input().split())
    fish[fx-1][fy-1].append(d-1)

sx,sy= map(int,input().split())
sx -= 1
sy -= 1
answer = 0

def copyFish():
    tmp = copy.deepcopy(fish)
    return tmp

def fishMove():
    global fish
    new = [[ [] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in fish[x][y]:
                nx,ny = x,y
                di = d
                for _ in range(8):
                    nx = x + dx[di]
                    ny = y + dy[di]
                    if 0<= nx < 4 and 0 <= ny < 4 and len(smell[nx][ny]) == 0 and not (sx==nx and sy == ny):
                        new[nx][ny].append(di)
                        break
                    else:
                        di -= 1
                        di %= 8
                else:
                    new[x][y].append(d)
    fish = new

def check(arr):
    arr = list(map(int,arr))
    tx,ty = sx,sy
    cnt = 0
    visited = [[0]*4 for _ in range(4)]
  
    for d in arr:
        tx += sdx[d]
        ty += sdy[d]
        if 0 <= tx < 4 and 0 <= ty < 4:
            if len(fish[tx][ty])> 0 and not visited[tx][ty]:
                cnt += len(fish[tx][ty])
                visited[tx][ty] = 1
        else:
            return -1
    return cnt

def sharkMove(arr):
    global fish, smell,sx,sy
    arr = list(map(int,arr))
    
    for d in arr:
        sx += sdx[d]
        sy += sdy[d]
        if len(fish[sx][sy]) > 0:
            fish[sx][sy] = []
            smell[sx][sy].append(nth)

def removeSmell():
    global smell
    if nth > 2:
        new = [[ [] for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for v in smell[i][j]:
                    if v != nth-2:
                        new[i][j].append(v)
        smell = new

def copyDone():
    global copied,fish
    for i in range(4):
        for j in range(4):
            for v in copied[i][j]:
                fish[i][j].append(v)
def choose(L,res):
    global cand
    if L == 3:
        cnt = check(res)
        if cnt != -1:
            cand.append((res, cnt))
        return
    for i in [0,1,2,3]:
        choose(L+1,res+str(i))
    

for nth in range(1,s+1):
    copied = copyFish()
    fishMove()
    cand = []
    choose(0,'')
    cand.sort(key=lambda x: (-x[1],x[0]))
    
    sharkMove(cand[0][0])
    removeSmell()
    copyDone()

for i in range(4):
    for j in range(4):
        answer += len(fish[i][j])
print(answer)