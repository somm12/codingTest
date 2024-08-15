g = [[[] for _ in range(4)] for _ in range(4)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def inRange(x,y):
    return 0 <= x < 4 and 0 <= y < 4

for i in range(4):
    tmp = list(map(int,input().split()))
    for j in range(0,8,2):
        g[i][j//2] = [tmp[j],tmp[j+1]-1]

def check(tmp,num):# 해당 위치에 물고기가 있는가.
    for x in range(4):
        for y in range(4):
            if tmp[x][y][0] == num:
                return [x,y]
    return False

def fishMove(tmp,sx,sy):# 물고기 이동.
    for num in range(1,17):
        value = check(tmp,num)
        if value != False:
            x,y = value
            nd = tmp[x][y][1]
            for _ in range(8):
                nx,ny= x+dx[nd],y+dy[nd]
                if inRange(nx,ny) and g[nx][ny][0] >= 0 and [nx,ny] !=[sx,sy]:
                    tmp[x][y][1] = nd# 방향전환.
                    tmp[x][y],tmp[nx][ny] = tmp[nx][ny],tmp[x][y]# 서로 위치 바꾸기
                    break
                nd = (nd+1)%8

def sharkMove(tmp,sx,sy,d):
    arr =[]
    nx,ny= sx,sy
    for _ in range(3):# 한번에 여러칸 가능 최대 3칸 넘기 가능.
        nx +=dx[d]
        ny += dy[d]
        if inRange(nx,ny) and tmp[nx][ny][0] >0 :# 물고기가 있어야만 함.
            arr.append((nx,ny))
    return arr
                    
def dfs(g,x,y,total):# 현재 격자판 상태, 상어위치, 지금까지의 잡아먹은 물고기 번호들의 합. x,y로 이동을 하려는 것.
    global answer 
    tmp = [[[] for _ in range(4)] for _ in range(4)]# 격자판 복사. 다음 재귀와의 혼선을 막기.
    for i in range(4):
        for j in range(4):
            tmp[i][j] = g[i][j][:]
    
    total += tmp[x][y][0]# 이동한 위치의 물고기 잡아먹기.
    tmp[x][y][0] = 0# 잡아먹었으니 빈칸으로 두기.
    d = tmp[x][y][1]# 상어가 가진 방향.
  
    fishMove(tmp,x,y)# 물고기 이동.
   
    arr =  sharkMove(tmp,x,y,d)# 상어 이동.
    if len(arr) ==0:# 더이상 이동불가면 끝.
        answer = max(answer,total)
        return
    for nx,ny in arr:
        dfs(tmp,nx,ny,total)
        

answer = 0
dfs(g,0,0,0)
print(answer)
        
# 백준 청소년상어