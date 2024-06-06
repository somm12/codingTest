from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer =0
R,C,k = map(int,input().split())
wood = [[0]*C for _ in range(R)]# 골렘 위치 기록 숲 지도.
exit = [[0]* C for _ in range(R)]# 탈출구 위치.
def inWood(x,y):
    return 0 <= x < R and 0 <= y < C
def check():# 제대로 된 숲 범위 내에 도착했는지 확인.
    x,y,di = boat
    if not inWood(x,y):
        return True
    for i in range(4):
        nx = x+dx[i]
        ny = y +dy[i]
        if not inWood(nx,ny):
            return True
    return False

def init():# 초기화.
    global wood, exit
    wood = [[0]*C for _ in range(R)]
    exit = [[0]*C for _ in range(R)]

def painting():# 최종 위치 기록.
    global wood,exit
    x,y,di = boat
    wood[x][y] = num
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        wood[nx][ny] = num
    ex,ey = x+dx[di],y+dy[di]
    exit[ex][ey] = num

def inRange(x,y):
    return -3 <= x < R and 0 <= y < C
def goDown():
    global boat
    boat[0] += 1
def goLeft():
    global boat
    boat[0] += 1
    boat[1] -= 1
    boat[2] = (boat[2] - 1) % 4
def goRight():
    global boat
    boat[0] += 1
    boat[1] += 1
    boat[2] = (boat[2] + 1)%4

def go():# 최하단까지 이동.
    while True:
        x,y,di = boat
        down = True
        for i,j in [(1,-1),(1,1),(2,0)]:
            nx = x+i
            ny = y+j

            if not inRange(nx,ny) or (inWood(nx,ny)and wood[nx][ny] != 0):# 움직일 때 초반에는 음수 행이 나오니 주의. 음수 행일 땐 통과, 숲 범위 내라면, 값이 0 인지 체크.

                down = False
                break
        if down:
            goDown()
            continue

        left = True
        for i,j in [(-1,-1),(0,-2),(1,-1),(2,-1),(1,-2)]:
            nx = x + i
            ny = y +j
            if not inRange(nx,ny) or (inWood(nx,ny)and wood[nx][ny] != 0):
                left = False
                break
        if left:
            goLeft()
            continue

        right = True
        for i,j in [(-1,1),(0,2),(1,1),(2,1),(1,2)]:
            nx = x + i
            ny = y +j
            if not inRange(nx,ny) or (inWood(nx,ny)and wood[nx][ny] != 0):
                right = False
                break
        if right:
            goRight()
            continue

        if not down and not left and not right:
            break

def move():# 이동.
    x,y,di = boat

    q= deque()
    ret = 0
    q.append((x,y,num))
    visited = [[0]*C for _ in range(R)]
    visited[x][y] = 1
    while q:

        px,py,nowNum = q.popleft()
        ret = max(ret,px)
        for i in range(4):
            nx,ny = px+dx[i],py+dy[i]
            if inWood(nx,ny) and not visited[nx][ny]:
                if wood[nx][ny] == nowNum or (exit[px][py] == nowNum and wood[nx][ny] > 0):
                    q.append((nx,ny,wood[nx][ny]))
                    visited[nx][ny] =1

    return ret + 1


for num in range(1,k+1):
    c,d = map(int,input().split())
    c -= 1
    boat = [-2,c,d]
    go()
    if check():
        init()
        continue
    painting()
    answer += move()

print(answer)

# 이동 구현시,
# 움직일 때 초반에는 음수 행이 나오니 주의. 음수 행일 땐 통과, 숲 범위 내라면, 값이 0 인지 체크.
# 따라서 숲 범위 내일 때, 밖일 때 나누어 if문 검사하기.
# 2:40 소요 디버깅 50분.

# 코드트리 문제