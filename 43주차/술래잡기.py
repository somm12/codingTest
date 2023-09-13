n,m,h,k = map(int,input().split())
dx = [-1,0,1,0]# 상 우 하 좌
dy = [0,1,0,-1]
tx = [1,0,-1,0] # 하우 상 좌 (거꾸로 0,0 => 중앙으로 갈 때)
ty = [0,1,0,-1]

runner = []
for _ in range(m):
    x,y,d = map(int,input().split())
    if d == 1:
        runner.append((x-1,y-1,1))
    else:
        runner.append((x-1,y-1,2))
tree = [[0]*n for _ in range(n)]

for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1

cx,cy,cd = n//2,n//2,0 # 술래 위치와 바라보는 방향
cidx = 0# 현재 술래 위치 인덱스.

answer =0 
location = [(cx,cy,cd)]# 술래가 이동할 모든 위치와 방향 정보를 담을 배열

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def getAllLocation():# 술래가 이동할 위치를 한 주기로 담은 배열 만들기.
    global location
    sx,sy = cx,cy
    d = 0
    cnt = 0
    while inRange(sx,sy):
        if d % 2 == 0:
            cnt += 1
        for i in range(cnt):
            sx += dx[d]
            sy += dy[d]
            if inRange(sx,sy):
                if i == cnt - 1:
                    location.append((sx,sy, (d+1)%4))
                else:
                    location.append((sx,sy, d))
        d = (d+1)%4
    location[-1] = (0,0,2)
    # 0,0 => 중앙 방향으로.
    sx,sy = 0,0
    d = 0
    cnt = n-1
    while True:
        if sx == n//2 and sy == n//2:
            break
        if d % 2 == 1:
            if not(cnt == n-1 and d == 1):# 처음에는 4 4 4 3 3 2 2 1 1 (2번씩 cnt만큼 이동, 하지만 초기에 1번만! 3번씩 이동.)
                
                cnt -= 1 
        for i in range(cnt):
            sx += tx[d]
            sy += ty[d]
            if not (sx == n//2 and sy == n//2):
                if i == cnt - 1:# 마지막 번째 이동시 방향 전환.
                    if (d+1)%4 == 0:
                        location.append((sx,sy, 2))
                    elif (d+1)%4 == 2:
                        location.append((sx,sy, 0))
                    else:
                        location.append((sx,sy, (d+1)%4))
                else:
                    if d == 0:
                        location.append((sx,sy, 2))
                    elif d == 2:
                        location.append((sx,sy, 0))
                    else:
                        location.append((sx,sy, d))
        d = (d+1)%4

def moveRunner():# 도망자 이동.
    global runner
    tmp = []
    for x,y,d in runner:
        if abs(cx-x) + abs(cy-y) <= 3:# 3칸 이내에 있다면 이동.
            nx = x+dx[d]
            ny = y+dy[d]
            if inRange(nx,ny):
                if cx == nx and cy == ny:# 술래가 있는 칸이면 가만히.
                    tmp.append((x,y,d)) 
                else:
                    tmp.append((nx,ny,d))
            else:# 격자밖일때
                d = (d+2)%4
                nx = x+dx[d]
                ny = y+dy[d]
                if not (cx == nx and cy == ny):# 방향 반대, 한칸이동 가능하면 이동.
                    tmp.append((nx,ny,d))
                else:
                    tmp.append((x,y,d))
        else:#! 이동을 안하는 runner.
            tmp.append((x,y,d))
    runner = tmp

def moveCatcher():# 술래 이동.
    global cidx,cx,cy,cd,runner,answer,location
    
    cidx = (cidx+1)% len(location)
    total = 0
    tmp = []
    
    cx,cy,cd = location[cidx]# 술래가 다음 위치로 이동
    nx,ny = cx,cy
    a = []# 술래가 감시하는 시야 좌표를 담은 배열.
    for _ in range(3):
        a.append((nx,ny))
        nx += dx[cd]
        ny += dy[cd]
        if not inRange(nx,ny):
            break
  
    for x,y,d in runner:
        if (x,y) in a and tree[x][y] == 0:# 시야내 & 나무가 없다면 잡힘.
            total += 1
        else:
            tmp.append((x,y,d))# 안잡힘
    answer += (turn* total)# 현재 턴 x 지금 턴에서 잡힌 도망자 수 만큼 점수 획득
    runner = tmp



getAllLocation()


for turn in range(1,k+1):
    
    moveRunner()
    moveCatcher()

print(answer)
# 삼성 기출
# 어느 범위 내에 있는가 => 배열에 할당해서 체크. 정확하게
# 달팽이 규칙 **: 반복 주기로 일차원 배열로 만들는 것.