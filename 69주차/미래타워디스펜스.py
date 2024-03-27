dx = [0,1,0,-1]
dy = [1,0,-1,0] #우 하 좌 상

n,m = map(int,input().split())
died = [0]*4

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

locat = {}
monster = []

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def init():
    global locat, monster
    x,y = n//2,n//2

    mx = [0,1,0,-1]
    my = [-1,0,1,0]

    di, cnt, idx = 0,0,0 # 방향 인덱스, 개수, locat인데스

    while inRange(x,y):
        if di % 2 == 0:
            cnt += 1
        for _ in range(cnt):
            x += mx[di]
            y += my[di]
            if inRange(x,y):
                if g[x][y] > 0:
                    monster.append(g[x][y])
                locat[(x,y)] = idx
                idx += 1
        di = (di+1) % 4


def attack():# d방향 p칸 만큼 삭제
    global monster,died

    x,y = n//2,n//2
    for _ in range(p):
        x = x + dx[d]
        y = y + dy[d]
        idx = locat[(x,y)]
        if idx < len(monster):
            died[monster[idx]] += 1
            monster[idx] = 0

def organize():# 중간에 빈 곳은 삭제.
    global monster

    tmp = []
    for v in monster:
        if v !=0:
            tmp.append(v)
    monster = tmp

def remove():
    global monster, died
    start = 0
    cnt = 0
    prev = monster[0]
    flag = False

    for i,v in enumerate(monster):# 같은 값 개수가 4개 이상이면 삭제.
        if prev == v:
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                died[prev] += cnt
                for idx in range(start,i):
                    monster[idx] = 0
            start = i
            cnt = 1
            prev = v
    if cnt >= 4:
        flag = True
        died[prev] += cnt
        for idx in range(start,start+cnt):
            monster[idx] = 0
    return flag

def change():
    global monster
    tmp = []
    prev = monster[0]
    cnt = 0

    for i,v in enumerate(monster):
        if prev == v:
            cnt += 1
        else:

            tmp.append(cnt)
            tmp.append(prev)
            prev = v
            cnt = 1

    tmp.append(cnt)
    tmp.append(prev)

    if len(tmp) >= n*n:# 격자 판 이상으로 길이가 늘어난다면 자르기.
        monster = tmp[:n*n]
    else:
        monster = tmp

init()# monster 배열에 나선 모양 순서로 값을 할당. locat딕셔너리에 좌표에 대한 monster 배열에서의 인덱스를 나타냄.

for nth  in range(1,m+1):
    d,p = map(int,input().split())
    attack()
    organize()
    if len(monster) == 0:# organize 이후 배열 길이가 0 이면 바로 종료. (몬스터 모두 죽음.)
        break
    while len(monster) > 0 and remove():
        organize()
    
    if len(monster) == 0:
        break
    change()

answer = 0
for i in range(1,4):
    answer += (died[i] * i)
print(answer)
