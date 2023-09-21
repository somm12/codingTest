from collections import defaultdict, deque

R,C,K = map(int,input().split())
g = []
wind = []
wall = defaultdict(list)
check = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
mx = [[-1,0,1], [-1,0,1], [-1,-1,-1],[1,1,1]]
my = [ [1,1,1], [-1,-1,-1], [-1,0,1], [-1,0,1]]

for i in range(R):
    g.append(list(map(int,input().split())))
    for j in range(C):
        if 1 <= g[i][j] <= 4:
            wind.append((i,j))
        elif g[i][j] == 5:
            check.append((i,j))

temp = [[0]*C for _ in range(R)]
W = int(input())

for _ in range(W):
    x, y, t = map(int,input().split())
    x -=1
    y -=1
    if t == 0:# 두 칸 간에 서로 벽이 있다는 표시로, 딕셔너리에 할당.
        wall[(x,y)].append((x-1,y))
        wall[(x-1,y)].append((x,y))
    else:
        wall[(x,y)].append((x,y+1))
        wall[(x,y+1)].append((x,y))

choco = 0

def go():# 온풍기 바람 퍼지기 시작.
    global temp
    for a,b in wind:
        idx = g[a][b] -1
        x,y = a+dx[idx], b+ dy[idx]
        temp[x][y] +=5
        visited = [[0]*C for _ in range(R)]
        visited[x][y] =1
        q= deque()
        q.append((x,y,5))
        if idx == 0:# 오른쪽 온풍기.
            while q:
                x,y,v = q.popleft()
                if v > 1:
                    for i in range(3):
                        nx = x+mx[idx][i]
                        ny = y+my[idx][i]
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                            if i == 0:# 오른 위
                                if (x-1,y) not in wall[(x,y)] and (x-1,y) not in wall[(x-1,y+1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = 1
                                    temp[nx][ny] += (v-1)
                            elif i == 1:# 오른쪽
                                if (x,y+1) not in wall[(x,y)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = 1
                                    temp[nx][ny] += (v-1)
                            else: # 오른 아래 방향.
                                if (x+1,y) not in wall[(x,y)] and (x+1,y) not in wall[(x+1,y+1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = 1
                                    temp[nx][ny] += (v-1)
        elif idx == 1:# 왼쪽.
            while q:
                x,y,v = q.popleft()
                if v > 1:
                    for i in range(3):
                        nx = x+mx[idx][i]
                        ny = y+my[idx][i]
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                            if i == 0:# 왼 위
                                if (x-1,y) not in wall[(x,y)] and (x-1,y) not in wall[(x-1,y-1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = 1
                                    temp[nx][ny] += (v-1)
                            elif i == 1:# 왼
                                if (x,y-1) not in wall[(x,y)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = 1
                                    temp[nx][ny] += (v-1)
                            else:# 왼아래.
                                if (x+1,y) not in wall[(x,y)] and (x+1,y) not in wall[(x+1,y-1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = 1
                                    temp[nx][ny] += (v-1)
        elif idx == 2:# 위쪽.
            while q:
                x,y,v = q.popleft()
                if v > 1:
                    for i in range(3):
                        nx = x+mx[idx][i]
                        ny = y+my[idx][i]
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                            if i == 0:#  위 왼
                                if (x,y-1) not in wall[(x,y)] and (x,y-1) not in wall[(x-1,y-1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = v-1
                                    temp[nx][ny] += (v-1)
                            elif i == 1:# 위 쪽
                                if (x-1,y) not in wall[(x,y)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = v-1
                                    temp[nx][ny] += (v-1)
                            else: # 위 오른
                                if (x,y+1) not in wall[(x,y)] and (x,y+1) not in wall[(x-1,y+1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = v- 1
                                    temp[nx][ny] += (v-1)
        else:# 아래.
            while q:
                x,y,v = q.popleft()
                if v > 1:
                    for i in range(3):
                        nx = x+mx[idx][i]
                        ny = y+my[idx][i]
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                            if i == 0:# 오른 위
                                if (x,y-1) not in wall[(x,y)] and (x,y-1) not in wall[(x+1,y-1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = v-1
                                    temp[nx][ny] += (v-1)
                            elif i == 1:# 오른쪽
                                if (x+1,y) not in wall[(x,y)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = v-1
                                    temp[nx][ny] += (v-1)
                            else:# 오른 위.
                                if (x,y+1) not in wall[(x,y)] and (x,y+1) not in wall[(x+1,y+1)]:
                                    q.append((nx,ny,v-1))
                                    visited[nx][ny] = v-1
                                    temp[nx][ny] += (v-1)


def control():# 온도조절 함수.
    global temp
    arr = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                # 두 지점 사이에 벽이 없다면 온도조절가능.
                if 0 <= nx < R and 0 <= ny < C and (nx,ny) not in wall[(x,y)]:
                   
                    diff = abs(temp[x][y]- temp[nx][ny])
                    tmp =diff//4
                    if temp[x][y] > temp[nx][ny]: # 한쪽이 더 크다면 tmp만큼 온도 감소, 작은 칸은 그만큼 증가.
                        arr[x][y] -= tmp
                        arr[nx][ny] += tmp
                    
    for x in range(R):# 증가 및 감소 업데이트.
        for y in range(C):
            temp[x][y] += arr[x][y]
def decrease():# 테두리 부분 -1 감소.
    global temp

    for j in range(C):
        if temp[0][j] > 0:
            temp[0][j] -= 1
        if temp[R-1][j] > 0:
            temp[R-1][j] -= 1
    for i in range(1,R-1):
        if temp[i][0] > 0:
            temp[i][0] -= 1
        if temp[i][C-1] >0:
            temp[i][C-1] -= 1
def isAllK():# 모두가 K이상인지 검사.
    for x,y in check:
        if temp[x][y] >= K:
            continue
        else:
            return False
    return True
while True:
    go()# 온풍기 퍼짐.
    control()# 온도조절.
    decrease()# 테두리 부분 -1.
    choco +=1
    if choco > 100:
        print(101)
        break
    if isAllK():# 조사할 부분이 모두 k이상인가.
        print(choco)
        break

# 삼성 기출.