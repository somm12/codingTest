n,m,k,c = map(int,input().split())
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cx = [-1,-1,1,1]
cy = [-1,1,1,-1]

spray = [[0]*n for _ in range(n)]
tree =[]
for _ in range(n):
    tree.append(list(map(int,input().split())))

def removeSpray():
    global spray
    
    for x in range(n):
        for y in range(n):
            if spray[x][y] == now:
                spray[x][y] = 0
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def grow():# 인접 4방향 나무 개수 만큼 동시에 성장.
    global tree
    tmp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tmp[x][y] = tree[x][y]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if inRange(nx,ny) and tree[nx][ny] > 0:
                        tmp[x][y] += 1
    tree = tmp

def spread():
    global tree
    tmp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tmp[x][y] = tree[x][y]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if inRange(nx,ny) and tree[nx][ny] == 0 and spray[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:
                    value = tree[x][y] // cnt# value 만큼 번식.
                    for i in range(4):
                        nx,ny = x+dx[i],y+dy[i]
                        if inRange(nx,ny) and tree[nx][ny] == 0 and spray[nx][ny] == 0:
                            tmp[nx][ny] += value

    tree = tmp

def find():
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
                        if inRange(nx,ny):
                            if tree[nx][ny] <= 0:
                                break
                            else:
                                cnt += tree[nx][ny]
                        else:
                            break
                cand.append((cnt,x,y))
    cand.sort(key =lambda x:(-x[0],x[1],x[2]))# 가장 많이 박멸, 가장 작은 행, 작은 열 순서.
    count, tx,ty = cand[0]# 박멸된 수, 위치.
    return [tx,ty,count]

def kill():
    global answer,tree,spray
    tx,ty,total = find()# 가장 많이 박멸되는 위칭 찾고, 박멸되는 수 반환.
    answer += total

    tree[tx][ty] = 0
    spray[tx][ty] = now + c+1# tx,ty 위치 값에는 해당 년도가 되면 스프레이가 사라짐.

    for i in range(4):
        nx,ny = tx,ty
        for _ in range(k):
            nx += cx[i]
            ny += cy[i]
            if inRange(nx,ny):
                if tree[nx][ny] <= 0:# 벽이나 빈칸을 만나면 그 칸까지만 뿌리고 끝.
                    spray[nx][ny] = now+c+1
                    break
                else:
                    tree[nx][ny] = 0
                    spray[nx][ny] = now+c+1
            else:
                break
    
def isFinish():
    cnt = 0
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt += 1
    return cnt == 0

for now in range(1,m+1):
    if isFinish():# 나무가 다 박멸되면 종료.
        break
    removeSpray()# 스프레이 제거
    
    grow()# 나무 성장
    
    spread()# 나무 번식
    kill()# 나무 박멸.
    

print(answer)
