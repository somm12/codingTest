n,m,h,k = map(int,input().split())
runner = []

dx = [-1,0,1,0]# 상 우 하 좌
dy = [0,1,0,-1]
for _ in range(m):
    x,y,d = map(int,input().split())
    if d == 1:# 좌우
        runner.append((x-1,y-1,1))
    else:
        runner.append((x-1,y-1,2))


tree = [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1
answer = 0
cx,cy = n//2, n//2
cd = 0
catcher = [(n//2,n//2,0)]
cidx = 0

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def getAllLocation():
    global catcher
    sx,sy = n//2,n//2 # 술래 첫위치.
    cnt = 0
    d = 0
    reversed = []
    while inRange(sx,sy):
        if d % 2 == 0:# 방향이 0또는 2가 될때, 해당 방향으로 움직이는 칸수가 1씩 증가.
            cnt += 1
        for i in range(cnt):
            sx += dx[d]
            sy += dy[d]
            if inRange(sx,sy):
                if i == cnt-1:#방향이 전환되는 시점
                    catcher.append((sx,sy,(d+1)%4))
                else:
                    catcher.append((sx,sy,d))
                reversed.append((sx,sy,(d+2)%4)) # 현재 칸의 방향(중앙 -> 0,0 경로)은 다음칸의 방향(0,0에서 중앙 경로) 반대 방향.

        d = (d+1)%4# 상 우 하 좌 형식으로 반복해서 방향이 변환.
    catcher = catcher[:-1] + reversed[::-1]# catcher에서 마지막인 (0,0)위치에서 방향은 아래방향이므로 제거. 그리고 반대방향인 reversed을 넣어줌.
    # 술래가 움직이게 될 위치와 방향 반복되는 한 주기를 담은 배열 만들기.

def moveRunner():# 도망자 이동.
    global runner
    newRunner = []# 도망자가 이동하고 난 이후, 도망자의 위치와 방향정보를 담은 배열.
    for x,y,d in runner:
        if abs(cx-x) + abs(cy-y) <=3:# 거리가 3이하만 이동 가능.
            nx = x+dx[d]
            ny = y +dy[d]
            if inRange(nx,ny):# 범위 내로 이동이 가능하면
                if nx == cx and ny == cy:# 술래가 있는 칸면 그대로
                    newRunner.append((x,y,d))
                else:
                    newRunner.append((nx,ny,d))# 아니면 이동.
            else:
                d = (d+2)%4 # 격자 밖으로 벗어날 경우,반대 방향을 가짐.
                nx = x+dx[d] 
                ny = y +dy[d]
                if nx == cx and ny == cy:# 방향 바꾼후, 한칸이동시 술래가 있다면.
                    newRunner.append((x,y,d))
                else:
                    newRunner.append((nx,ny,d)) # 술래가 없다면. 이동.
        else:
            newRunner.append((x,y,d)) # 이동할 대상이 아닐때.
    runner = newRunner # 바뀐 위치 배열 업데이트.

def moveCatcher():# 술래가 이동.
    global answer, runner,cidx,cx,cy,cd
    total = 0 # 잡힌 도망자수
    newRunner = []
    cidx = (cidx+1)%len(catcher) # 다음 위치로 이동.
    cx,cy,cd = catcher[cidx]

    tmp = []# 3칸에 해당하는 위치 배열.
    nx,ny = cx,cy
    for _ in range(3):# 현재칸 포함해서 해당 방향으로 3칸 내에 있는 도망자 제거.
        tmp.append((nx,ny))
        nx += dx[cd]
        ny += dy[cd]
        if inRange(nx,ny):
            continue
        else:
            break
    for x,y,d in runner:# 도망자가 3칸 이내 위치한다면 제거.
        if (x,y) in tmp and tree[x][y] == 0:# 나무에 가려져 있지 않고, 시야내에 해당하면 제거.
            total += 1 # 잡힌 도망자수 구하기.
        else:
            newRunner.append((x,y,d))# 살아남음.
    answer += (turn*total)# 점수 획득.
    runner = newRunner# 도망자 위치 배열 다시 업데이트.
        
getAllLocation() # 술래가 움직일 수 있는 모든 좌표와 위치.


for turn in range(1,k+1):
    moveRunner()
    moveCatcher()
print(answer)
# 술래잡기 풀이 다른 방식으로 풀기.