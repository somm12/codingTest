
dx = [-1,1,0,0]
dy = [0,0,-1,1]

direction = [0]# 현재 플레이어의 위치
turn = 1

n,m,k = map(int,input().split())
info = [[[] for _ in range(n)] for _ in range(n)]# 플레이어의 번호, 유효기간
player = [[[] for _ in range(4)] for _ in range(m+1)]# 각 플레이어의 방향 우선 순위.
locat = {}#현재플레이어 위치


g = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] > 0:
            g[i][j].append(a[j])
            info[i][j] = [a[j],k]
            locat[a[j]] = [i,j]
        else:
            info[i][j] = [0,0]
    
for v in list(map(int,input().split())):# 현재 플레이어 방향
    direction.append(v-1)

for i in range(4*m):# 플레이어 이동 방향 우선 순위 입력.
    arr = list(map(int,input().split()))
    for v in arr:
        player[(i//4)+1][i%4].append(v-1)

def check():
    if len(locat) == 1 and 1 in locat:
        return True
    return False

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def endContract():
    global info
    for x in range(n):
        for y in range(n):
            if info[x][y][1] < turn:
                info[x][y] = [0,0]

def move():
    global g,direction ,locat
    
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    
    for num in locat:
        x,y = locat[num]
        
       
        cand = []
        for i in range(4):# 아무도 없는 칸.
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and info[nx][ny][0] == 0:
                cand.append((nx,ny,i))
        if len(cand) == 0:# 아무도 없는 칸이 없다면, 독점 계약한 칸을 우선순위 방향대로 선택.
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if inRange(nx,ny) and info[nx][ny][0] == num:
                    cand.append((nx,ny,i))
            c = False
            for d in player[num][direction[num]]:
                for nx,ny,nd in cand:
                    if d== nd:
                        tmp[nx][ny].append(num)
                        direction[num] = nd
                        locat[num] = [nx,ny]
                        c = True
                        break
                if c:
                    break
        else:
            c = False
            for d in player[num][direction[num]]:
                for nx,ny,nd in cand:
                    if d== nd:
                        tmp[nx][ny].append(num)
                        direction[num] = nd
                        locat[num] = [nx,ny]
                        c = True
                        break
                if c:
                    break       
    g = tmp

def remove():
    global g,locat
    newG = [[[] for _ in range(n)] for _ in range(n)]
    for num in range(1,m+1):
        if num in locat:
            x,y = locat[num]
            
            if len(g[x][y]) >= 1 and len(newG[x][y]) == 0:#*****
                newG[x][y].append(num)
        
           
    g = newG
    tmp = {}
    for x in range(n):
        for y in range(n):
            if len(g[x][y]) > 0:
                num = g[x][y][0]
                tmp[num] = [x,y]
    locat = tmp


def doContract():
    global info
    for num in locat:   
        x,y = locat[num]
        info[x][y] = [num, k+ turn]



while True:
  
    if turn > 1000:
        print(-1)
        break
    if check():
        print(turn -1)
        break
    endContract()
    
    move()
    remove()
    doContract()
    turn += 1

