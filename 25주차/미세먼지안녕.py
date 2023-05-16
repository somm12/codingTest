n,m,t = map(int,input().split())
g = []
cleaner =[]
answer = 0
cnt = 0
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if g[i][j] == -1:# 청정기 위치를 담아둠
            cleaner.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 미세먼지 확산 함수. A(r,c)//5 만큼 퍼지고, 퍼진 방향 수 만큼 -A(r,c)로 먼지양이 줄어듦.
def spread():
    global g
    dust = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                tmp = g[x][y]//5
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != -1:
                        dust[nx][ny] += tmp
                        g[x][y] -= tmp
    for x in range(n):
        for y in range(m):
            g[x][y] += dust[x][y]
# 공기 순환시키기.
def fresh():
    global g
    new = [[0]*m for _ in range(n)] # 순환 후 모습을 담을 new 배열.
    for i in range(n):
        for j in range(m):
            new[i][j] = g[i][j]
    # 청정기 위쪽 방향은 우 상 좌 하 방향으로 순환
    dx1 = [0,-1,0,1]
    dy1 = [1,0,-1,0]
    # 청정기 아래 방향은 우 하 좌 상 방향으로 순환.
    dx2 = [0,1,0,-1]
    dy2= [1,0,-1,0]
    # 첫 시작 위치 : 공기청정기 바로 옆쪽 칸
    sx1,sy1 = cleaner[0][0], (cleaner[0][1]+1)
    sx2,sy2 = cleaner[1][0], (cleaner[1][1]+1)
    # 첫 부분은 미세먼지가 옮겨져서 0 이 됨
    new[sx1][sy1] = 0
    new[sx2][sy2] = 0

    # 각 아래방향 위쪽 방향에 대해서 4가지 방향으로 공기가 순환됨.
    for i in range(4):
        while True:
            nx = sx1+dx1[i]
            ny = sy1+dy1[i]
            # 범위를 벗어나거나 공기 청정기를 만났을 때, 순환을 멈추고 이어서 다음 방향으로 순환.
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != -1:
                new[nx][ny] = g[sx1][sy1]
            else:
                break
            sx1=nx
            sy1 = ny
        while True:
            nx = sx2+dx2[i]
            ny = sy2+dy2[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != -1:
                new[nx][ny] = g[sx2][sy2]
            else:
                break
            sx2=nx
            sy2 = ny
    # 순환 후 배열을 재할당.
    g = new

    
while True:
    spread()
    fresh()
   
    cnt += 1
    # T초 후 공기 순환 멈춤.
    if t== cnt:
        break


# 마지막으로, 남은 먼지의 양을 계산
for i in range(n):
    for j in range(m):
        if g[i][j] > 0:
            answer += g[i][j]
print(answer)