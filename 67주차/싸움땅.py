n,m,k = map(int,input().split())
g = [[[] for _ in range(n)] for _ in range(n)]
locat = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        g[i][j].append(arr[j])

player = {}
point = [0]*(m+1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(1,m+1):
    x,y,d,s = map(int,input().split())
    player[i] = [x-1,y-1,d,s,0]
    locat[x-1][y-1].append(i)

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move():
    global player,locat

    x,y,d,s,gun = player[num]
    nx,ny = x+dx[d],y + dy[d]
    if inRange(nx,ny):
        player[num]= [nx,ny,d,s,gun]
        locat[x][y].pop()
        locat[nx][ny].append(num)
        return [nx,ny]
    
    nd = (d+2)%4
    nx,ny = x+dx[nd], y+dy[nd]
    player[num] = [nx,ny,nd,s,gun]

    locat[x][y].pop()
    locat[nx][ny].append(num)
    return [nx,ny]

def getGun(now):
    global g, player
    x,y,d,s,gun = player[now]
    g[x][y].append(gun)
    g[x][y].sort()
    player[now][-1] = g[x][y].pop()

def fight():
    global point

    p1,p2 = locat[nextX][nextY]
    
    s1,gun1 = player[p1][3],player[p1][4]
    s2,gun2 = player[p2][3], player[p2][4]
    t1 = s1+gun1
    t2 = s2+gun2

    if t1 > t2:
        point[p1] += (t1-t2)
        return [p1,p2]
    elif t1 < t2:
        point[p2] += (t2 - t1)
        return [p2,p1]
    else:
        if s1 > s2:
            return [p1,p2]
        return [p2,p1]
    
def lose(l):
    global g,locat
    x,y,d,s,gun = player[l]
    if gun > 0:
        g[x][y].append(gun)
    nx,ny = x+dx[d],y +dy[d]

    if not inRange(nx,ny) or len(locat[nx][ny]) > 0:
        nd = d
        for _ in range(4):
            nd = (nd+1)%4
            nx, ny = x+dx[nd], y +dy[nd]
            if inRange(nx,ny) and len(locat[nx][ny]) == 0:
                player[l] = [nx,ny,nd,s,0]# 격자에 총을 두고 떠나므로 0을 넣는다.
                locat[nx][ny].append(l)
                locat[x][y].remove(l)
                break
    else:
        locat[nx][ny].append(l)
        locat[x][y].remove(l)
        player[l] = [nx,ny,d,s,0]
    
    getGun(l)

def win(w):
    getGun(w)

for nth in range(1,k+1):
    for num in range(1,m+1):
        nextX,nextY = move()
        if len(locat[nextX][nextY]) <=1:
            getGun(num)
           
        else:
            w,l = fight()
            lose(l)

            win(w)
for i in range(1,m+1):
    print(point[i],end= ' ')
