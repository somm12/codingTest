n,m,k,c = map(int,input().split())
tree = []
for _ in range(n):
    tree.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
mx = [-1,1,-1,1]
my = [1,1,-1,-1]
info = [[0]*n for _ in range(n)]

def inRange(x,y):
    return 0<=x<n and 0 <= y < n
def allDie():
    cnt = 0
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt += 1
    return cnt == 0

def removeSpray():
    global info
    for x in range(n):
        for y in range(n):
            if info[x][y] == year:
                info[x][y] = 0
def grow():
    global tree
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    if inRange(nx,ny) and tree[nx][ny] > 0:
                        cnt += 1
                tree[x][y] += cnt
def spread():
    global tree
    tmp = [v[:] for v in tree]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                arr = []
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if inRange(nx,ny) and tree[nx][ny] == 0 and info[nx][ny] == 0:
                        arr.append((nx,ny))
                if len(arr)>0:
                    num = tree[x][y]//len(arr)
                    for a,b in arr:
                        tmp[a][b] += num
    tree =tmp
def find():
    global answer
    cand = []
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                total = tree[x][y]
                for i in range(4):
                    nx,ny =x,y
                    for _ in range(k):
                        nx += mx[i]
                        ny += my[i]
                        if not inRange(nx,ny) or tree[nx][ny] <= 0:
                            break
                        if tree[nx][ny] > 0:
                            total += tree[nx][ny]
                cand.append((total,x,y))
    cand.sort(key=lambda x:(-x[0],x[1],x[2]))
    x,y = cand[0][1],cand[0][2]
    answer += cand[0][0]
    return [x,y]
def spray(tx,ty):
    global info,tree
    tree[tx][ty] = 0
    info[tx][ty] = year+c
    for i in range(4):
        nx,ny=tx,ty
        for _ in range(k):
            nx += mx[i]
            ny += my[i]
            if not inRange(nx,ny):
                break
            if tree[nx][ny] <= 0:# 나무가 없는 칸 또는 벽을 만난 다면 해당 칸까지 뿌리고 끝.
                info[nx][ny] = year+c
                break
            else:# 나무가 있는 곳.
                tree[nx][ny] = 0
                info[nx][ny] = year+c

answer = 0
for year in range(1,m+1):
    if allDie():
        break
    grow()
    spread()

    tx,ty = find()
    spray(tx,ty)
    removeSpray()
print(answer)