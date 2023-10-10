n,m,k,c = map(int,input().split())

tree =[]
for _ in range(n):
    tree.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1] # 인접 4칸 상하 좌우

cx = [-1,-1,1,1]
cy = [-1,1,1,-1]#대각선 4방향 .
pill = [[0]*n for _ in range(n)] # 제초제

answer =0

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def grow():# 나무가 동시에 인접 4방향 중 나무가 있는 칸 수 만큼 성장.
    global tree

    tmp = [arr[:] for arr in tree]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                for i in range(4):
                    nx = dx[i]+x
                    ny = dy[i] +y
                    if inRange(nx,ny) and tree[nx][ny] > 0:
                        tmp[x][y] += 1
    tree =tmp

def spread():# 인접한 4칸 중에서 (해당 칸 나무수//완전히 빈칸(제초제도 없음) 개수) 만큼, 인접한 완전한 빈칸에 번식.
    global tree
    tmp = [arr[:] for arr in tree]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if inRange(nx,ny) and tree[nx][ny] == 0 and pill[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:
                    value = tree[x][y] // cnt
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y+dy[i]
                        if inRange(nx,ny) and tree[nx][ny] == 0 and pill[nx][ny] == 0:
                            tmp[nx][ny] += value
    tree = tmp

def reduceSpray():# 제초제 1년 지남을 -1 만큼 감소로 표현.
    global pill
    for x in range(n):
        for y in range(n):
            if pill[x][y] > 0:
                pill[x][y] -= 1

def choose():# 제초제 뿌릴 위치 선정, 대각선 4방향으로 k만큼 가장 많이 박멸되고, 행이 작고, 열이 작은 순서.
    global answer # 중간에 빈칸 또는 벽이 나오면 멈춤.
    cand = []
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = tree[x][y]

                for i in range(4):
                    nx,ny = x,y
                    for _ in range(k):
                        nx += cx[i]
                        ny += cy[i]
                        if not inRange(nx,ny):# 격자 밖
                            break
                        else:
                            if tree[nx][ny] > 0:# 나무가 존재
                                cnt += tree[nx][ny]
                            else:# 빈칸 또는 벽
                                break
                cand.append((cnt,x,y))

    cand.sort(key=lambda x:(-x[0],x[1],x[2]))
    x,y = cand[0][1],cand[0][2]
    answer += cand[0][0]# 해당 개수만큼 나무 박멸.
    return [x,y]

def spray(x,y):# 제초제 뿌리기. 나무가 죽고, 제초제가 c년 만큼 유지.
    global pill, tree
    tree[x][y] = 0# 먼저 뿌릴 칸 처리 하기.
    pill[x][y] =c

    for i in range(4):
        nx,ny = x,y
        for _ in range(k):
            nx += cx[i]
            ny += cy[i]
            if not inRange(nx,ny):
                break
            if tree[nx][ny] <= 0:# 벽이나 빈칸이라면 해당 칸까지만 제초제 뿌리고 멈춤.
                if tree[nx][ny] == 0:# 빈칸에 제초제 뿌림. 벽은 안뿌려도 ok.
                    pill[nx][ny] = c
                break
            else:# 나무가 있는 칸 처리 하기.
                tree[nx][ny] = 0
                pill[nx][ny] =c

def isAllDied():# 하나라도 나무가 남아있다면 False.
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                return False
    return True
    
for t in range(1,m+1):
    if isAllDied():# 나무가 더이상 없다면 종료. => 더이상 박멸할 수 있는 나무가 없으므로
        break
    grow()# 성장
    spread()# 번식
    reduceSpray()# 제초제 뿌렸던 부분 -1
    a,b = choose()# 제초제를 뿌릴 좌표 선정
    spray(a,b)# 제초제 뿌리기.
  
print(answer)# 총 박멸한 나무 수.


