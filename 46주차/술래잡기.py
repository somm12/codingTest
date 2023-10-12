n,m,h,k = map(int,input().split())
runner = []
for _ in range(m):
    x,y,d = map(int,input().split())
    runner.append((x-1,y-1,d))
tree = [[0]*n for _ in range(n)]

for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1

cd, cidx, cx,cy = 0,0,n//2,n//2
dx = [-1,0,1,0]
dy= [0,1,0,-1]
dest = []# 술래가 이동하는 좌표 및 바라보는 방향 정보 한 주기를 담을 배열 
answer = 0

def init():# 술래가 이동하는 좌표와 위치 를 한 주기로 만들어 배열에 할당.
    global dest
    cnt = 0
    nx,ny= n//2,n//2
    d = 0

    while 0 <= nx < n and 0 <= ny < n:
        if d % 2 == 0:
            cnt += 1
        for _ in range(cnt):
            dest.append((nx,ny,d))## (중앙점 부터 시작.)
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < n):
                break

        d = (d+1)%4
    dest.pop()
    dest.append((0,0,2))# 1행 1열 부분은 방향이 아래쪽이므로 수정.

    # 거꾸로 (끝에서 중앙으로)
    tmp = dest[::-1]
    tmp = tmp[1:]
    reversedArr = []
    for i in range(len(tmp)-1):
        x,y,d = tmp[i]
        nx,ny,nd = tmp[i+1] 
        reversedArr.append((x,y,(nd+2)%4))# 다음 방향의 반대 방향.
    dest += reversedArr


def inRange(x,y):
    return 0<= x < n and 0 <= y < n

def runnerMove():# 도망자 이동.
    global runner
    new = []
    for x,y,d in runner:
        dist = abs(cx-x) + abs(cy-y)
        if dist <= 3:
            nx = x+dx[d]
            ny = y+dy[d]
            if inRange(nx,ny):
                if [nx,ny] == [cx,cy]:
                    new.append((x,y,d))
                else:
                    new.append((nx,ny,d))
            else:
                nd = (d+2)%4
                nx = x+dx[nd]
                ny = y+dy[nd]
                if [nx,ny] != [cx,cy]:
                    new.append((nx,ny,nd))
                else:
                    new.append((x,y,nd))
        else:
            new.append((x,y,d))
    runner = new

def catcherMove():
    global cx,cy,cidx,cd
    L = len(dest)
    cidx = (cidx+1)%L
    cx,cy,cd = dest[cidx]

def watch():
    global answer,runner
    tx,ty = cx,cy
    cnt = 0
    catched = {}

    for _ in range(3):
        if 0 <= tx < n and 0 <= ty < n:
            for x,y,d in runner:
                if [tx,ty] == [x,y] and tree[tx][ty] == 0:
                    catched[(x,y)] =1
                    cnt += 1
            tx += dx[cd]
            ty += dy[cd]
    newRunner = []
    for x,y,d in runner:# 잡히지 않은 도망자만 따로 다시 runner에 할당.
        if (x,y) not in catched:
            newRunner.append((x,y,d))
    runner = newRunner
    answer += (turn * cnt)

init()

for turn in range(1,k+1):
    if len(runner) == 0:# 도망자가 없다면 끝냄
        break
    runnerMove()
    catcherMove()
    watch()

print(answer)