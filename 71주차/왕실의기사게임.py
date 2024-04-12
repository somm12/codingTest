from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
L,N,Q = map(int,input().split())
point = [0]*(N+1)
player = {}
g = []
locat = [[0]*L for _ in range(L)]
for _ in range(L):
    g.append(list(map(int,input().split())))
for num in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    r -= 1
    c -= 1
    arr = []
    for i in range(r,r+h):
        for j in range(c,c+w):
            arr.append((i,j))
            locat[i][j] = num
    player[num] = [arr,k]

def inRange(x,y):
    return 0 <= x < L and 0<= y < L

def move(number,di):# number번 기사 이동.
    global player, locat
    q = deque()
    q.append(number)
    changed = set()# 움직이는 기사 번호를 담은 집합.

    while q:
        nowNum = q.popleft()
        if nowNum not in changed:
            changed.add(nowNum)
        tmp = set()# 지금 기사가 움직였을 때, 밀리는 다른 기사를 담을 집합
        for x,y in player[nowNum][0]:
            nx = x+dx[di]
            ny = y+dy[di]
            if inRange(nx,ny):
                if g[nx][ny] == 2:# 벽을 만나면 모든 기사 움직임은 없음.
                    return False
                if locat[nx][ny] > 0 and locat[nx][ny] != nowNum:# 다른 누군가가 있다면.
                    tmp.add(locat[nx][ny])
            else:# 벽을 만나면 움직임X
                return False
        for v in tmp:# 밀려서 움직이게 되는기사들 큐에 넣기.
            q.append(v)
    #변경사항 반영
    changed = list(changed)

    for v in changed:
        tmp = []
        for x,y in player[v][0]:
            nx = x+dx[di]
            ny = y+dy[di]
            tmp.append((nx,ny))
        player[v][0] = tmp

    newLocat = [[0]*L for _ in range(L)]# 기사들 배포된 상황을 다시 새로 반영.
    for number in player:
        for x,y in player[number][0]:
            newLocat[x][y] = number
    locat = newLocat


    return changed

def demage(arr):
    global player,locat,point
    deleted = set()
    for number in arr:# 움직인 기사들.
        if number != num:# 명령받은 기사는 제외
            cnt = 0
            for x,y in player[number][0]:
                if g[x][y] == 1:# 함정 개수 만큼 체력이 깎임.
                    cnt += 1
            if player[number][1] <= cnt:# 현재 체력 이상으로 깎인다면 격자에서 사라짐.
                del player[number]
                deleted.add(number)# 사라지는 기사들 번호를 따로 담는다.
            else:
                player[number][1] -= cnt
                point[number] += cnt
    for x in range(L):# 기사들 위치 정보를 담은 locat에 사라진 기사 반영하기.
        for y in range(L):
            if locat[x][y] in deleted:
                locat[x][y] = 0

for nth in range(1,Q+1):
    
    num,d = map(int,input().split())
    if num not in player:# 사라진 기사라면 명령 무시.
        continue

    moved = move(num,d)# 이동.
    
    if moved != False:
        demage(moved)# 피해를 입음.
    
answer = 0
for num in player:
    answer += point[num]# 살아남은 기사들의 피해 총합.
print(answer)