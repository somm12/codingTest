n,m,k = map(int,input().split())
g = [[]*n for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for v in arr:
        g[i].append([v])

player= {}
locat = [[[] for _ in range(n)] for _ in range(n)]
point = [0]*(m+1)
for i in range(1,m+1):
    x,y,d,s = map(int,input().split())
    player[i] = [x-1,y-1,d,s,0]
    locat[x-1][y-1].append(i)
dx = [-1,0,1,0]
dy =[0,1,0,-1]

def move():
    global player
    x,y,d,s,gun = player[num]
    nx,ny = x+dx[d],y+dy[d]
    if inRange(nx,ny):
        player[num] = [nx,ny,d,s,gun]
        locat[x][y].pop()
        locat[nx][ny].append(num)
        return [nx,ny]
    nd = (d+2)%4
    nx,ny = x+dx[nd],y+dy[nd]
    player[num] = [nx,ny,nd,s,gun]
    locat[x][y].pop()
    locat[nx][ny].append(num)
    return [nx,ny]
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def getGun(x,y,p):# 해당 위치에 p번 플레이어가 총을 획득한다면.
    global g,player
    
    if len(g[x][y]) > 0:
        guns = g[x][y]
        pg = player[p][4]
        arr = guns + [pg]
        arr.sort()
        player[p][4] = arr[-1]# 제일 큰 능력의 총을 획득. 나머지는 내려둔다.
        g[x][y] = arr[:-1]
def winner(p):
    x,y = player[p][0], player[p][1]
    getGun(x,y,p)

def fight():
    global point
    people = locat[nx][ny]
    p1,p2 = people
    tmp1 = player[p1][3] + player[p1][4]
    tmp2 = player[p2][3] + player[p2][4]
    if tmp1 > tmp2:
        point[p1] += (tmp1 - tmp2)# 차이 만큼 점수 획득.
        return [p1,p2]
    elif tmp1 < tmp2:
        point[p2] += (tmp2 -tmp1)
        return [p2,p1]
    else:# 점수 합이 같으면 초기 능력 으로 비교.
        if player[p1][3] > player[p2][3]:
            return [p1,p2]
        return [p2, p1]
def loser(p):# p번 플레이저 지면,
    global player,locat
    x,y,d,s,gun = player[p]
    locat[x][y].remove(p)# 다른 방향으로 이동.
    if gun > 0:# 총을 내려둔다.
        g[x][y].append(gun)
        gun = 0 
    nx,ny = x+dx[d],y+dy[d]# 바로방향으로 이동.

    if not inRange(nx,ny) or len(locat[nx][ny]) > 0:# 오타 주의. 누군가 있거나 격자 밖일때.

        for _ in range(4):
            d = (d+1)%4# 오른쪽 90 방향으로 움직이다 빈 곳으로 바로 이동.
            nx,ny = x+dx[d],y+dy[d]
            if inRange(nx,ny) and len(locat[nx][ny]) == 0:
                locat[nx][ny].append(p)
                player[p] = [nx,ny,d,s,gun]
                getGun(nx,ny,p)# 이동 이후, 총 획득.
                break
    else:# 다음 칸에 아무도 없다면
        locat[nx][ny].append(p)
        player[p] = [nx,ny,d,s,gun]# 변동 시킬 때, 변수 사용 조심.
        getGun(nx,ny,p)

for round in range(k):
    for num in range(1,m+1):# 순서대로 이동.
        nx,ny = move()
        if len(locat[nx][ny]) <= 1:# 누군가가 없다면
            
            getGun(nx,ny,num)
         
        else:# 누군가 있다면 싸움.
            
            w,l = fight()# 진 사람 이긴 사람 번호 반환.
            
            loser(l)# 진 사람 처리
            winner(w)# 이긴 사람 처리
        

  
for i in range(1,m+1):
    print(point[i],end=' ')