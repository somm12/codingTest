import copy

n,m,k,c = map(int,input().split())
tree = []
for _ in range(n):
    tree.append(list(map(int,input().split())))
answer = 0
dx = [-1,1,0,0]# 상 하 좌 우. 인접한 칸.
dy = [0,0,-1,1]
mx = [-1,-1,1,1] # 대각선 4방향.
my = [-1,1,1,-1]

spray = [[0]*n for _ in range(n)]# 제초제 양이 들은 배열.

def grow():# 인접한 4칸에 나무가 있는 수 만큼 나무가 성장.
    global tree
    tmp = copy.deepcopy(tree)
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] > 0:
                        tmp[x][y] += 1
    tree = tmp

def spread():# 동시에 나무가 번식. 인접 4칸 중에 벽과 제초제, 다른 나무가 없는 칸의 개수 만큼 나누어 퍼짐.
    global tree
    tmp = copy.deepcopy(tree)
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < n and 0 <= ny < n and tree[nx][ny]== 0 and spray[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:# 개수가 있을 때만 나누어 퍼짐. divide zero 에러 조심.
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y +dy[i]
                        if 0 <= nx < n and 0 <= ny < n and tree[nx][ny]== 0 and spray[nx][ny] == 0:
                            tmp[nx][ny] += (tree[x][y]//cnt)
    tree = tmp


def choose():# 제초제 뿌릴 위치 좌표와, 제거될 나무 개수 반환.
    cand = []
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                total = 0
                total += tree[x][y]
                for i in range(4):
                    nx,ny = x,y
                    for _ in range(k):
                        nx += mx[i]
                        ny += my[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            if tree[nx][ny] == 0:# 나무가 아예없으면 그 칸 까지만 뿌리고 그만.
                                total += tree[nx][ny]
                                break
                            elif tree[nx][ny] == -1:# 도중에 벽 만나면 거기서 그만
                                break
                            else:
                                total += tree[nx][ny]
                cand.append((x,y,total))
    cand.sort(key = lambda x:(-x[2],x[0],x[1]))
    if cand:
        return cand[0]
    return [-1,-1,-1]

def reduceSpray():# 해가 지날때 마다 제초제 -1씩 줄이기. 제초제 뿌릴 때, 이미 제초제가 있다면 새로 뿌린게 기준이므로,먼저 줄이기.
    global spray
    for i in range(n):
        for j in range(n):
            if spray[i][j] > 0:
                spray[i][j] -= 1

def kill(x,y):# 제초제를 뿌리고 나무 죽이기.
    global tree,spray
    tree[x][y] = 0
    spray[x][y] = c # 뿌릴 위치에 먼저 제초제 뿌리기!
    for i in range(4):
        nx,ny = x,y
        for _ in range(k):
            nx += mx[i]
            ny += my[i]
            if 0 <= nx < n and 0 <= ny < n:
                if tree[nx][ny] == 0 : #나무가 없는 칸이면 거기까지만.
                    spray[nx][ny] = c
                    tree[nx][ny] = 0
                    break
                elif tree[nx][ny] == -1:# 벽을 만나도 거기까지만.
                    break
                else:
                    spray[nx][ny] = c
                    tree[nx][ny] = 0
    
for _ in range(m):#m년 동안 반복.
    grow()# 나무 성장
    spread()# 나무 번식
    x,y,total = choose()# 제초제 뿌릴 칸 선정
    reduceSpray()# 제초제 -1
    if [x,y,total] != [-1,-1,-1]:# 제초제를 뿌릴나무가 있는 거라면,
        answer += total# 제거할 나무 개수 구하기.
        kill(x,y) # 제초제 뿌리기.

print(answer)
# 전역변수와 변수명이 겹치지 않도록.
# 제출 전 테스트케이스와 동일한지 확인.