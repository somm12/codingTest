n,m,k =map(int,input().split())
gun = [[] for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for v in arr:
        gun[i].append([v])
player = {}

for i in range(1,m+1):
    x,y,d,s = map(int,input().split())
    player[i] = [x-1,y-1,d,s,0]
point= [0]*(m+1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def other(x,y,num):# 격자 칸에 또다른 사람이 있는지 확인
    for i in player:
        a,b,_,_,_ = player[i]
        if [a,b] == [x,y] and num != i:
            return i
    return 0
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move(num):# 이동하려면 방향으로 이동, 격자 벗어나면, 반대 방향으로 한칸 이동
    global player
    x,y,d,s,g = player[num]
    nx = x+dx[d]
    ny = y+dy[d]
    if not inRange(nx,ny):
        d = (d+2)%4
        nx = x+dx[d]
        ny = y+dy[d]
        player[num] = [nx,ny,d,s,g]
    else:
        player[num] = [nx,ny,d,s,g]
    return [nx,ny]

def getScore(now,otherNum):# 현재 차례인 now 번 사람과 otherNum사람이 싸워서 점수 획득.
    global point
    x1,y1,d1,s1,g1 = player[num]
    x2,y2,d2,s2,g2 = player[otherNum]
    v1 = s1+g1
    v2 = s2+g2

    if v1 > v2:
        point[num] += abs(v1-v2)
        return [otherNum, now]# 진 번호, 이긴 번호 반환 .
    elif v1 < v2:
        point[otherNum] += abs(v1-v2)
        return [now, otherNum]
    else:# 값이 같다면 초기 능력치랑 비교 .
        if s1 < s2:
            return [now,otherNum]
        return [otherNum,now]
def lose(num):
    global player,gun
    x,y,d,s,g = player[num]
    if g > 0:# 총 내려두기
        gun[x][y].append(g)
        player[num][4] = 0
    nx = x+dx[d]
    ny = y+dy[d]
    if not inRange(nx,ny) or other(nx,ny,num):
        for _ in range(4):
            d=(d+1)%4
            nx = x+dx[d]
            ny = y+dy[d]
            if inRange(nx,ny) and not other(nx,ny,num):
                maxGun = max(gun[nx][ny])
                if maxGun > 0:# 총이 있으면
                    gun[nx][ny].remove(maxGun) # 획득 하기 !
                    if len(gun[nx][ny]) == 0: # 빼냈는데 아무 것도 없다면 빈칸 의미로 0 넣기.
                        gun[nx][ny].append(0)
                player[num] = [nx,ny,d,s,maxGun]
                break
    else:

        maxGun = max(gun[nx][ny])
        if maxGun > 0:# 총이 있으면
            gun[nx][ny].remove(maxGun) # 획득 하기 !
            if len(gun[nx][ny]) == 0:
                gun[nx][ny].append(0)
        player[num] = [nx,ny,d,s,maxGun]
def win(num):# 이겼을 때.
    global gun,player
    x,y,d,s,g = player[num]

    maxGun = max(gun[x][y])

    if maxGun > g:# 가지고 있던 총 vs 칸에 놓여져 있는 총들 중 가장 큰 값. 제일 큰 값을 획득한다.
        gun[x][y].remove(maxGun) 
        player[num][4] = maxGun

        gun[x][y].append(g)# 나머지 내려두기

def getGun(num):
    global gun,player
    x,y,d,s,g = player[num]

    maxGun = max(gun[x][y])

    if maxGun > g:
        gun[x][y].remove(maxGun)
        player[num][4] = maxGun
        gun[x][y].append(g)# 내려두기


for i in range(1,k+1):
    for num in range(1,m+1):
        a,b = move(num)
        otherNum = other(a,b,num)# 누가 있는지 체크, 값이 0 이면 없는것 아니라면 누가 있는것

        if otherNum > 0:# 누가 있다면, 싸워서 점수 획득, 진번호, 이긴 번호 차례로 처리하기.
            l,w = getScore(num,otherNum)
            lose(l)
            win(w)
        else:
            getGun(num) # 누가 없다면, 해당 칸에 있는 가장 공격력이 큰 총과 가지고 있던 총 중 큰 총 획득.

for i in range(1,m+1):
    print(point[i],end =' ')