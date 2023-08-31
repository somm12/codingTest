n,m,k = map(int,input().split())
gun = [ [[] for _ in range(n)] for _ in range(n) ]

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] != 0:
            gun[i][j].append(a[j])
player = []
point = [0]*(m+1)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(1,m+1):
    x,y,d,s = map(int,input().split())
    player.append((i,x-1,y-1,d,s,0))
def getPos(num):# num 번호를 가진 player가 이동할 위치, 방향 및 정보들을 반환.
    for a in player:
        if a[0] == num:
            numb,x,y,d,s,p = a
            break
    mx = x+dx[d]
    my = y+dy[d]
    if 0 <= mx < n and 0 <= my < n:
        return [mx,my,d,s,p]
    d += 2# 격자 밖을 벗어나면 반대 방향으로 이동
    d %= 4
    mx = x+dx[d]
    my = y+dy[d]
    return [mx,my,d,s,p]

def check(nx,ny):# 해당 nx,ny 칸에 다른 플레이어가 있는지 확인.
    for v in player:
        if nx == v[1] and ny == v[2]:
            return True
    return False

def fight(nx,ny,num):# nx,ny에 싸움이 일어남. 현재 num번호 차례 진행중.
    global point
    for v in player:
        if nx == v[1] and ny == v[2] and v[0]!= num:
            num2,x2,y2,d2,s2,p2 = v
        elif v[0]== num:
            num1,x1,y1,d1,s1,p1 = v
    diff = abs( (s1+p1) - (s2+p2))# 초기 능력치 + 총의 공격력 => 차이 값이 포인트로 획득됨.
    if s1+p1 > s2+p2:
        w = num1
        l = num2
    elif s1+p1 < s2+p2:
        w= num2
        l = num1
    else:# 총 공격력 + 초기 능력치 합이 같다면, 초기 능력치를 비교
        if s1 > s2:
            w = num1
            l = num2
        else: 
            w = num2
            l = num1
    point[w] += diff # 이긴 번호 포인트 획득.
    return [w,l] # 이긴 번호와 진 번호반환

def update(num,info):# num 번호를 가진 player의 정보를 update
    global player
    x,y,d,s,p=info
    for i in range(m):
        if player[i][0] == num:
            player[i] = (num,x,y,d,s,p) 
            break

def takeGun(x,y,add):# x,y 좌표에 해당하는 총 격자판에 add 만큼의 공격력을 추가.(가진 총 공격력과 격자에 있던 총 공격력 중 최대값 구하기)
    global gun
    gun[x][y].append(add) # 추가하기.
    gun[x][y].sort(reverse=True)# 큰 순으로 정렬
    p = gun[x][y].pop(0)# 큰 값은 pop

    return p   # 큰 공격력 반환.
def lose(l): # 진 번호의 정보를 찾고,
    for i in range(m):
        if player[i][0] == l:
            numb,x,y,d,s,p = player[i]
            break
    
    gun[x][y].append(p) # 가진 총 내려두기.
    
    mx = x + dx[d] # 한칸으로 이동
    my = y + dy[d]
    if check(mx,my) or not (0<= mx < n and 0 <= my < n): # 격자 밖 / 누가 있다면
        for _ in range(4): # 오른쪽으로 회전하면서 격자 밖이 아니며, 누가 없는 칸으로 이동.
            d += 1
            d %= 4
            mx = x + dx[d]
            my = y + dy[d]
            if 0 <= mx < n and 0 <= my < n and not check(mx,my):
                # 이동 가능 칸을 발견하면, 해당 칸의 가장 큰 총의 공격력 반환.
                p = takeGun(mx,my,0) # 총을 내려두었기 때문에, 0을 추가. 
                
                info = (mx,my,d,s,p)# 해당 칸과 반환된 총의 공격력으로 update.
                update(l,info)
                break # 격자 범위내이면서 다른 누가 없는 칸이 보이는 순간 이동.
    else:
        p = takeGun(mx,my,0)
        info = (mx,my,d,s,p)
        update(l,info)

def win(w):# 이긴 번호의 정보를 찾고, 해당 격자 칸에 가장 공격력이 큰 총의 공격력을 얻는다.
    for v in player:
        if v[0] == w:
            numb,x,y,d,s,p = v
            break
    p = takeGun(x,y,p)
    info = (x,y,d,s,p)
    update(w,info)

for i in range(1,k+1):
    for num in range(1,m+1):
        
        nx,ny,dir,s,p = getPos(num) # 이동할 위치 정보.
        
        isExist = check(nx,ny) # 해당 위치에 누군가 있는지 확인.
        if isExist: # 누가 있다면 싸움. 
            info = (nx,ny,dir,s,p)
            update(num, info) # 이동할 위치로 update
            w,l = fight(nx,ny,num) # 싸워서 진 번호와 이긴 번호 반환
            lose(l) # 진 번호 처리
            win(w) # 이긴 번호 처리
        else:
            p = takeGun(nx,ny,p) # 해당 칸에 총을 내려두고, 가장 큰 공격력을 가진 값 반환.
            info = (nx,ny,dir,s,p) 
            update(num,info) # 해당 총 공격력과 이동한 정보로 update
        
        
for i in range(1,m+1):
    print(point[i],end=' ')