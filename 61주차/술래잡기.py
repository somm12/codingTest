n,m,h,k = map(int,input().split())
runner = {}
tree = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]# 상 우 하 좌
dy = [0,1,0,-1]
for i in range(1,m+1):
    x,y,d = map(int,input().split())
    if d == 1:# 좌우
        runner[i] =[x-1,y-1,1]
    elif d == 2:# 상하
        runner[i] = [x-1,y-1,2]
for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1

answer = 0
pattern =[]# 술래가 움직이는 패턴
cx,cy,cd,cidx = n//2,n//2,0,0 # 술래의 현재 위치, 바라보는 방향, 패턴에서의 인덱스
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def init():
    global pattern
    x,y = n//2, n//2
    cnt = 0
    d = 0
    while 0 <= x < n and 0 <= y < n:# 상 우 하 좌 (1번 1번 2번 2번 ,, 만큼씩 이동.)
        if d % 2 == 0:
            cnt += 1
        for _ in range(cnt):
            if inRange(x,y):
                pattern.append([x,y,d])
            x += dx[d]
            y += dy[d]
        
        d = (d+1)%4
    
    reversedP = []
    
    for x,y,d in pattern[::-1]:# 반대 형태의 모습을 담기 => 참조 값이 같아져서 복사가 제대로 되지 않을 수 있음에 대비.
        reversedP.append([x,y,d])

    for i in range((n*n)-1):# 현재 위치가 바라보는 방향은 다음 위치가 바라보는 방향의 반대.
        di = (reversedP[i+1][2] + 2)%4
        reversedP[i][2] = di
    
    
    pattern = pattern[:-1]# 마지막 (0,0) 부분은 빼기
    reversedP = reversedP[:-1]# 마지막 (중앙 지점) 부분은 빼기
    for arr in reversedP:
        x,y,d = arr
        pattern.append([x,y,d])# 패턴을 합침
    

def runnerMove():
    global runner
    tmp = {}
    for num in runner:
        x,y,d = runner[num]
        diff = abs(x-cx) + abs(y-cy)
        
        if diff <= 3:# 술래와 거리가 3 이하인 도망자만 이동.
        
            nx,ny = x +dx[d],y+dy[d]
            if inRange(nx,ny):
                if [cx,cy] == [nx,ny]:
                    tmp[num] = [x,y,d]
                else:
                    tmp[num] = [nx,ny,d]
            else:# 격자 밖일때
                nd = (d+2)%4
                nx,ny = x+dx[nd],y+dy[nd]
                if [nx,ny] != [cx,cy]:
                    tmp[num] = [nx,ny,nd]
                else:
                    tmp[num] = [x,y,nd]
        else:#이동안함
            tmp[num] = [x,y,d]
    runner = tmp

def catcherMove():
    global cx,cy,cd, cidx, answer, runner
    tmp = {}

    cidx = (cidx+1)% len(pattern)
    cx,cy,cd = pattern[cidx]

    scope = [(cx,cy)]# 시야 범위
    nx,ny = cx,cy
    for _ in range(2):
        nx += dx[cd]
        ny += dy[cd]
        if inRange(nx,ny):
            scope.append((nx,ny))
    cnt = 0# 잡히는 도망자 수
    for num in runner:
        x,y,d = runner[num]
        if (x,y) in scope and tree[x][y] == 0:# 나무에 가려진 도망자는 잡히지 않음.
            cnt += 1
        else:
            tmp[num] = [x,y,d]
    runner = tmp
    answer += (t*cnt)# 현재 턴 x 현재 턴에서 잡힌 도망자 수 만큼 점수가 더해짐.

init()# 술래의 이동 패턴을 구하기.
for t in range(1,k+1):
    if len(runner) < 1:# 도망자가 더 이상 없다면 점수도 더 생기지 않으므로 break.
        break
    runnerMove()
    catcherMove()
print(answer)