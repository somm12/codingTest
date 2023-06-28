from collections import deque
r,c,k = map(int,input().split())

house = []
choco = 0
target = [] # 조사할 칸 담을 배열
machine = [] # 온풍기 위치
wall = [[[] for _ in range(c)] for _ in range(r)] # x,y에 벽이 있는지 확인하기 위한 배열.
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 오 왼 위 아래
mx = [[-1,0,1],[-1,0,1],[-1,-1,-1],[1,1,1]] # 바람이 퍼질 때 3 가지 방향.
my = [[1,1,1],[-1,-1,-1],[1,0,-1],[1,0,-1]]

for i in range(r):
    house.append(list(map(int,input().split())))
    for j in range(c):
        t = house[i][j]
        if 1 <= t <= 4:
            machine.append((i,j,t-1)) # 온풍기 위치와 방향 입력.
        elif t == 5:
            target.append((i,j)) # 검사할 칸 정보 입력.
# 벽 위치 입력받기.
w = int(input())
for _ in range(w):
    x,y,t = map(int,input().split())
    x -= 1 # 0,0 부터 시작! **
    y -= 1
    if t == 0:
        wall[x][y].append((x-1,y)) # 서로 사이에 벽이 있으므로, 두 좌표에 각각 할당.
        wall[x-1][y].append((x,y))
    else:
        wall[x][y].append((x,y+1))
        wall[x][y+1].append((x,y))

temp = [[0]*c for _ in range(r)] # 온도 상태를 담을 배열

def wind():
    for x,y,d in machine:# 온풍기 하나씩 진행.
        spread(x,y,d)
        

def spread(x,y,d):
    global temp
    q = deque()
    visited = [[0]*c for _ in range(r)]
    nx = x + dx[d]
    ny = y + dy[d]
    q.append((nx,ny,5)) # 맨처음 온풍기 방향 한 칸은 항상 5도.
    temp[nx][ny] += 5
    visited[nx][ny] = 1 # 이미 방문한 곳은 피하기 위해 방문 처리.
    
    while q:
        x,y,t = q.popleft()
        for i in range(3):# 오른 위, 오른, 오른 아래. 3방향으로 퍼짐.
            nx = x + mx[d][i]
            ny = y + my[d][i]
            if 0<= nx < r and 0 <= ny < c and not visited[nx][ny] and t > 1: # 온도가 1이면 퍼져도 0이라 제외
                if d == 0:
                    if i == 0: # 오른쪽 위쪽방향 
                        if (x-1,y) not in wall[x][y] and (x-1,y+1) not in wall[x-1][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 1: # 오른쪽
                        if (x,y+1) not in wall[x][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 2: # 오른쪽 아래
                        if (x+1,y) not in wall[x][y] and (x+1,y+1) not in wall[x+1][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                elif d == 1: #왼쪽 방향.
                    if i == 0: # 왼위
                        if (x-1,y) not in wall[x][y] and (x-1,y-1) not in wall[x-1][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 1: # 왼
                        if (x,y-1) not in wall[x][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
            
                    elif i == 2: # 왼 아래
                        if (x+1,y) not in wall[x][y] and (x+1,y) not in wall[x+1][y-1]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                elif d == 2:
                    if i == 0: # 위 오른
                        if (x,y+1) not in wall[x][y] and (x,y+1) not in wall[x-1][y+1]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 1: # 위
                        if (x-1,y) not in wall[x][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 2: # 위 왼
                        if (x,y-1) not in wall[x][y] and (x,y-1) not in wall[x-1][y-1]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                elif d == 3: # 아래
                    if i == 0: # 아래 오른
                        if (x,y+1) not in wall[x][y] and (x,y+1) not in wall[x+1][y+1]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 1: # 아래
                        if (x+1,y) not in wall[x][y]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                    elif i == 2: # 아래 왼
                        if (x,y-1) not in wall[x][y] and (x,y-1) not in wall[x+1][y-1]:
                            temp[nx][ny] += (t-1)
                            visited[nx][ny] = 1
                            q.append((nx,ny,t-1))
                        

def tempControl():# 온도 조절. 벽이 있으면 조절 X! **
    global temp
    new = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            new[i][j] = temp[i][j] # 복사하기

    for x in range(r):
        for y in range(c):
            now = temp[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i] # 범위 이내, 벽이 없다면
                if 0 <= nx < r and 0 <= ny < c and (nx,ny) not in wall[x][y]:
                    near = temp[nx][ny]
                    if now > near:
                        v = (now-near) // 4
                        new[nx][ny] += v # 낮은 온도는 차이//4만큼 증가
                        new[x][y] -= v # 높은 온도는 차이//4만큼 감소
    temp = new

def outline(): # 테두리 부분 온도가 1이상이면 -1
    global temp
    for x in [0,r-1]:
        for y in range(c):
            if temp[x][y] >= 1:
                temp[x][y] -= 1
    for x in range(1,r-1):
        for y in [0,c-1]:
            if temp[x][y] >= 1:
                temp[x][y] -= 1
def eatChoco():
    global choco
    choco += 1
def check(): # 검사할 칸 모두 k이상 온도면 True 반환. 종료.
    for x, y in target:
        if temp[x][y] >= k:
            continue
        else:
            return False
    return True
    
while True:
    wind() # 온풍기 작동, 온도가 퍼진다.
    tempControl() # 온도 조절
    outline() # 테두리 부분 -1
    eatChoco() # 초콜릿 먹기
    if choco > 100: # 100을 넘어가면 종료.
        break
    if check(): # 혹시 검사할 칸 모두 온도가 k이상이라면 종료.
        break
print(choco)

# 벽 조건, 문제 이해, 입력받을 때 -1 하는지 확인. 중요.