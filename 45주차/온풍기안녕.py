from collections import deque
R,C,K = map(int,input().split())
wall = {}
choco = 0
check= []# 조사할 칸
temp = []# 온풍기 정보들
g = []

dx = [0,0,-1,1]# 오 왼 위 아래
dy = [1,-1,0,0]
mx = [[-1,0,1],[-1,0,1],[-1,-1,-1], [1,1,1]]
my = [[1,1,1],[-1,-1,-1],[-1,0,1],[-1,0,1]]

for i in range(R):
    g.append(list(map(int,input().split())))
    for j in range(C):
        if 1 <= g[i][j] <= 4:
            temp.append((i,j,g[i][j]-1))
        elif g[i][j] == 5:
            check.append((i,j))
W = int(input())
for _ in range(W):
    x,y,t = map(int,input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall[(x,y,x-1,y)] =1
        wall[(x-1,y,x,y)] =1
    else:
        wall[(x,y,x,y+1)] = 1
        wall[(x,y+1,x,y)] =1
g = [[0]*C for _ in range(R)] # 온도를 저장할 배열로 다시 초기화 *** 이부분 실수.
def move():
    global g
    for x,y,d in temp:
        q = deque()
        nx = x+dx[d]
        ny = y+dy[d]
        q.append((nx,ny,5))
        g[nx][ny] += 5
        visited = [[0]*C for _ in range(R)]
        visited[nx][ny] = 5
        while q:
            a,b, t = q.popleft()
            if t > 1:# 1 이하라면, 더이상 퍼질 필요 없음.
                for i in range(3):
                    nx = a+ mx[d][i]
                    ny = b+ my[d][i]
                    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                        if d == 0:#오른쪽
                            if i == 0:# 오른쪽 위 
                                if (a,b,a-1,b) not in wall and (a-1,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                            elif i == 1:# 오른쪽  
                                if (a,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                            else:# 오른쪽 아래
                                if (a,b,a+1,b) not in wall and (a+1,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                        if d==1:# 왼
                            if i ==0:
                            # 왼위
                                if (a,b,a-1,b) not in wall and (a-1,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                            elif i == 1:#왼
                                if (a,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)


                            else:# 왼아래
                                if (a,b, a+1,b) not in wall and (a+1,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                        if d == 2:# 위
                            if i == 0:# 위왼
                                if (a,b,a,b-1) not in wall and (a,b-1, nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                            elif i == 1:#위
                                if (a,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)

                            else:#위오른
                                if (a,b,a,b+1) not in wall and (a,b+1,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)
                        if d == 3:# 아래
                            if i == 0:#아래왼
                                if (a,b,a,b-1) not in wall and (a,b-1,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)
                            elif i == 1:#아래
                                if (a,b,nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)
                            else:#아래 오른
                                if (a,b,a,b+1) not in wall and (a,b+1, nx,ny) not in wall:
                                    q.append((nx,ny,t-1))
                                    visited[nx][ny] = 1
                                    g[nx][ny] += (t-1)
def control():# 인접한 4칸에서 온도차이//4 만큼, 큰 칸은 감소, 작은 칸은 증가.
    global g
    newG = [arr[:] for arr in g]
    visited = {} # 방문처리를 위함.
    for x in range(R):
        for y in range(C):
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < R and 0 <= ny < C and (x,y,nx,ny) not in visited and (x,y,nx,ny) not in wall:
                    visited[(x,y,nx,ny)] =1
                    visited[(nx,ny,x,y)]=1
                    diff = abs(g[x][y] - g[nx][ny])//4
                    if g[x][y] > g[nx][ny]:
                        newG[nx][ny] += diff
                        newG[x][y] -= diff
                    elif g[x][y] < g[nx][ny]:
                        newG[x][y] += diff
                        newG[nx][ny] -= diff
    g = newG

def decrease():
    global g
    for j in range(C):
        if g[0][j] > 0:
            g[0][j] -= 1
        if g[R-1][j] > 0:
            g[R-1][j] -= 1
    for i in range(1,R-1):
        if g[i][0] > 0:
            g[i][0] -= 1
        if g[i][C-1] > 0:
            g[i][C-1] -= 1
def isFinish():
    flag = True
    for x,y in check:
        if g[x][y] < K:
            flag= False
    return flag

while True:
    if choco > 100:
        print(101)
        break
    move()# 바람 이동

    control()# 온도 조절

    decrease()# 테두리 부분 -1

    choco += 1

    if isFinish():# 조사할 칸이 모두 K이상이면 종료.
        print(choco)
        break
# 바람이 퍼질때, 온도조절 부분 => 겹치지 않게 방문처리 부분 유의하기.
# 벽 부분 조건 실수하지 않도록 유의
# 삼성 기출 문제