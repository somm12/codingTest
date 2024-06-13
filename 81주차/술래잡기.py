n,m,h,k = map(int,input().split())
runner = {}
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(1,m+1):
    x,y,d = map(int,input().split())
    runner[i] = [x-1,y-1,d]

tree = [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1


cx,cy,cd,cidx = n//2,n//2,0,0# 술래의 위치와 바라보는 방향 & 술래가 이동하는 패턴을 가리키는 인덱스.
pattern = []

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def init():
    global pattern
    cnt = 0
    di =0
    direct = -1
    x,y = n//2,n//2
    while inRange(x,y):
        if di % 2==0:
            cnt += 1
        for _ in range(cnt):
            if inRange(x,y):
                pattern.append((x,y,di))
            else:
                break
            x += dx[di]
            y += dy[di]
        di = (di+1)%4
    #반대
    pattern = pattern[:-1]
    pattern.append((0,0,2))
    tmp = []
    for i in range(len(pattern)-2,0,-1):
        x,y,di = pattern[i]
        nx,ny,nd = pattern[i-1]
        tmp.append((x,y,(nd+2) % 4))
    pattern = pattern + tmp

def rMove():
    global runner
    for num in runner:
        x,y,di = runner[num]
        dist = abs(cx-x) + abs(cy-y)
        if dist > 3:
            continue
        nx,ny = x+dx[di],y+dy[di]
        if inRange(nx,ny):
            if nx == cx and ny == cy:
                continue
            else:
                runner[num][0],runner[num][1] = nx,ny
        else:
            nd = (di+2)%4
            nx,ny = x+dx[nd],y+dy[nd]
            if not (nx == cx and ny == cy):
                runner[num] = [nx,ny,nd]
            else:
                runner[num] = [x,y,nd]

def cMove():
    global cx,cy,cd,cidx
    cidx = (cidx+1)% len(pattern)
    cx,cy,cd = pattern[cidx]

def catch():
    global answer,runner
    tmp ={}
    locat = set()
    nx,ny= cx,cy
    for _ in range(3):
        locat.add((nx,ny))
        nx += dx[cd]
        ny += dy[cd]
    cnt =0
   
    for num in runner:
        x,y,di = runner[num]
        if (x,y) in locat and tree[x][y] == 0:
            cnt += 1
        else:
            tmp[num] = [x,y,di]# 잡히지 않는 경우
 
    answer += (t*cnt)
    runner = tmp

answer = 0
init()

for t in range(1,k+1):
    if len(runner) ==0:
        break
    rMove()
    cMove()
    catch()

print(answer)

