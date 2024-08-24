R,C,T = map(int,input().split())
g = []
c =[]
for i in range(R):
    g.append(list(map(int,input().split())))
    for j in range(C):
        if g[i][j] == -1:
            c.append(([i,j]))

rdx =[0,-1,0,1]# 반시계 방향 바람 순환
rdy = [1,0,-1,0]

dx = [0,1,0,-1]# 시계 방향 바람 순환
dy = [1,0,-1,0]

def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

def spread():
    global g
    tmp = [v[:] for v in g]# 동시에 퍼지므로, 원래 배열 복사.
    for x in range(R):
        for y in range(C):
            if g[x][y] > 0:
                cnt = 0
                value = g[x][y]//5
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if inRange(nx,ny) and g[nx][ny] >= 0:
                        cnt += 1
                        tmp[nx][ny] += value
                tmp[x][y] -= (value * cnt)# 퍼진 방향 개수 만큼 빼고 남은 양이 됨.
    g = tmp
                
def clean():
    global g
    tmp = [v[:] for v in g]
    #반시계
    sx,sy = c[0][0],1
    d = 0
    while True:
        nx,ny = sx+rdx[d],sy+rdy[d]
        
        if inRange(nx,ny):
            if g[nx][ny] == -1: break# 청정기 만나게 되면 끝. 먼지가 빨려들어감.
            tmp[nx][ny] = g[sx][sy]
        else:
            d = (d+1)%4
            nx,ny = sx+rdx[d],sy+rdy[d]
            tmp[nx][ny] = g[sx][sy]
        sx,sy = nx,ny
    tmp[c[0][0]][1] = 0# 순환 뒤에 첫 시작점은 0으로 두기.
    # 시계
    d = 0
    sx,sy = c[1][0],1
    while True:
        nx,ny = sx+dx[d],sy+dy[d]
        if inRange(nx,ny):
            if g[nx][ny] == -1: break
            tmp[nx][ny] = g[sx][sy]
        else:
            d = (d+1)%4
            nx,ny = sx+dx[d],sy+dy[d]
            tmp[nx][ny] = g[sx][sy]
        sx,sy = nx,ny
    tmp[c[1][0]][1] = 0
    
    g = tmp
    
time= 0 
while time < T:
    spread()# 먼지 퍼짐
   
    clean()# 정화시작
    
    time +=1
    
answer =0
for x in range(R):
    for y in range(C):
        if g[x][y] > 0:
            answer += g[x][y]

print(answer)
# 백준 미세먼지 안녕