n,m,k = map(int,input().split())
g = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        g[i][j].append(arr[j])
player = {}
person = [[[] for _ in range(n)] for _ in range(n)]# 격자에 있는 사람들 번호를 담을 3차원 배열.
for i in range(1,m+1):
    x,y,d,s= map(int,input().split())
    player[i] = [x-1,y-1,d,s,0]
    person[x-1][y-1].append(i)

dx = [-1,0,1,0]# 상 우 하 좌.
dy = [0,1,0,-1]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move(number):# 이동.
    global player, person
    x,y,d,s,gun = player[number]
    nx = x+dx[d]
    ny = y +dy[d]
    if inRange(nx,ny):# 격자 내라면, 방향대로 한 칸 이동.
        player[number] = [nx,ny,d,s,gun]
        person[x][y].pop()# 위치 이동.
        person[nx][ny].append(number)
    else:
        nd = (d+2)%4# 격자 밖이라면 방향을 반대로 해서 이동.
        nx = x+dx[nd]
        ny = y+dy[nd]
        player[number] = [nx,ny,nd,s,gun]# 위치 및 방향 업데이트.
        person[x][y].pop()
        person[nx][ny].append(number)

def takeGun(number):# 가장 쎈 총 획득.
    global player,g
    x,y,d,s,gun = player[number]
    g[x][y].append(gun)
    g[x][y].sort()
    newGun = g[x][y].pop()
    player[number] = [x,y,d,s,newGun]

def fight(x,y):# x,y에 위치한 플레이어 끼리 싸움. 이긴 사람은 초기 능력치+총 능력 차이 만큼 점수 획득.
    global point
    n1,n2 = person[x][y]
    _,_,_,s1,gun1 = player[n1]
    _,_,_,s2,gun2 = player[n2]
    diff = abs((s1+gun1) - (s2+gun2))

    if s1+gun1 > s2+gun2:
        point[n1] += diff
        return [n1,n2]
    elif s1+gun1 < s2+gun2:
        point[n2] += diff
        return [n2,n1]
    else:
        if s1 > s2:
            return [n1,n2]
        return [n2,n1]

def win(number):
    takeGun(number)

def lose(number):# 진사람은 총을 버리고, 한 칸이동(다른 사람이 있거나 격자 밖이면 90도 오른쪽회전하며, 가능한 칸으로 이동.)
    global player,person,g
    x,y,d,s,gun = player[number]
    g[x][y].append(gun)
    player[number][4] = 0
    nx =x+dx[d]
    ny = y+dy[d]

    if not inRange(nx,ny) or len(person[nx][ny]) >0:
        nd =d
        for _ in range(4):
            nd = (nd+1)%4
            nx = x+dx[nd]
            ny = y+dy[nd]
            if inRange(nx,ny) and len(person[nx][ny]) == 0:
                player[number][0],player[number][1],player[number][2] = nx,ny,nd
                person[x][y].remove(number)
                person[nx][ny].append(number)
                takeGun(number)
                break
    else:
        player[number][0],player[number][1] = nx,ny
        person[x][y].remove(number)
        person[nx][ny].append(number)
        takeGun(number)

point = [0]*(m+1)
for nth in range(1,k+1):
    for num in range(1,m+1):
        move(num)

        px,py,_,_,_ = player[num]
        if len(person[px][py]) == 1:
            takeGun(num)
        else:
            w,l = fight(px,py)
            lose(l)
            win(w)
        
for i in range(1,m+1):
    print(point[i],end=' ')

