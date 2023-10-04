from collections import defaultdict

n,m,k = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

g = []
player = {}
location = {}
keep = [[0]*n for _ in range(n)]# 남은 계약기간을 담을 배열
host = [[0]*n for _ in range(n)]# 계약 된 칸이 누구 땅인제 번호를 담일 배열.

for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] > 0:
            num = g[i][j]
            # num -= 1
            player[num] = [i,j]
            location[(i,j)] = [num]
            keep[i][j] = k
            host[i][j] = num
direction = list(map(int,input().split()))

for i,v in enumerate(direction):
    player[i+1].append(v-1)
priority = [[] for _ in range(m)]

for i in range(4*m):
    a,b,c,d = map(int,input().split())
    priority[i//4].append([a-1,b-1,c-1,d-1])
turn = 1

def over():# 계약 기간 -1. 끝나게 되면 host는 0
    global host,keep
    for i in range(n):
        for j in range(n):
            if keep[i][j] > 0:
                keep[i][j] -= 1
                if keep[i][j] == 0:
                    host[i][j] = 0

def move():# 각 주어진 방향의 우선순위에 따라서, 아무 계약이 없는 땅 > 자신이 계약한 땅을 순서로 이동.
    global player, location, keep, host
    np = {}
    nl = defaultdict(list)

    for num in player:

        x,y,d = player[num]
        isMoved=False
        for i in priority[num-1][d]:
            nx = x+dx[i]
            ny =y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and host[nx][ny] == 0:# 그 누구도 계약하지 않은 땅이 있으면 이동.
                np[num] = [nx,ny,i]
                nl[(nx,ny)].append(num)
                isMoved = True
                break
        if not isMoved:
            for i in priority[num-1][d]:
                nx = x+dx[i]
                ny =y+dy[i]
                if 0 <= nx < n and 0 <= ny < n and host[nx][ny] == num:# 아니면 자신의 독점 땅으로 이동.
                    np[num] = [nx,ny,i]
                    nl[(nx,ny)].append(num)

                    break
    player=np
    location=nl

def remove():# 한 칸에 두명이 들어가면 가장 낮은 번호를 제외하고 삭제.
    global keep,host,location,player
    nl = {}
    np = {}
    for x,y in location:
        num = min(location[(x,y)])# 가장 작은 번호인 플레이어.
        if len(location[(x,y)]) >=2:
            np[num] = player[num]
            nl[(x,y)] = [num]
        else:
            np[num] = player[num]
            nl[(x,y)] = [num]
    location = nl
    player = np
    # 제거 한 이후, 최종적으로 이동한 상태에서 땅 독점 계약 갱신
    for num in player:
        x,y,d = player[num]
        host[x][y] = num
        keep[x][y] = k
def check():# 1번 만 남는지 확인.
    return len(player) == 1

while True:
    if turn >1000:# 1000 번이 넘으면 -1.
        print(-1)
        break

    move()# 이동

    over()# 독점 기간 -1

    remove()# 한칸에 두명이면 제거 . 가장 작은 번호만 살아남는다.

    if check():# 1번만 남았는지 체크
        print(turn)
        break
    turn += 1


