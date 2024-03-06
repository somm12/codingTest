n,m,k,c = map(int,input().split())
tree =[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cx = [-1,-1,1,1]
cy =[-1,1,-1,1]

for _ in range(n):
    tree.append(list(map(int,input().split())))

spray = [[0]*n for _ in range(n)]
answer = 0

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def grow():
    global tree
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                for i in range(4):
                    nx,ny = x+dx[i],y + dy[i]
                    if inRange(nx,ny) and tree[nx][ny] > 0:
                        tree[x][y] += 1

def spread():
    global tree
    tmp = [arr[:] for arr in tree]
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = 0
                value = tree[x][y]
                for i in range(4):
                    nx,ny = x+dx[i],y +dy[i]
                    if inRange(nx,ny) and tree[nx][ny] == 0 and spray[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:
                    for i in range(4):
                        nx,ny = x+dx[i],y +dy[i]
                        if inRange(nx,ny) and tree[nx][ny] == 0 and spray[nx][ny] == 0:
                            tmp[nx][ny] += (value//cnt)
    tree = tmp

def findSpot():
    global answer
    cand = []
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                total = tree[x][y]
                for i in range(4):
                    nx,ny = x,y
                    for _ in range(k):
                        nx += cx[i]
                        ny += cy[i]
                        if inRange(nx,ny):
                            if tree[nx][ny] <= 0:
                                break
                            else:
                                total += tree[nx][ny]
                        else:
                            break
                cand.append((total, x,y))
    cand.sort(key = lambda x :(-x[0],x[1],x[2]))
    total,x,y = cand[0]
    answer += total
    return [x,y]
def kill(x,y):
    global tree,spray
    spray[x][y] = now+c
    tree[x][y] = 0
    for i in range(4):
        nx,ny = x,y
        for _ in range(k):
            nx += cx[i]
            ny += cy[i]
            if inRange(nx,ny):
                if tree[nx][ny] <= 0:# 나무가 없거나 벽이면 그 칸까지 제초제를 뿌린다.
                    spray[nx][ny] = now+c
                    break
                else:
                    spray[nx][ny] = now+c
                    tree[nx][ny] = 0
            else:
                break

def removeSpray():
    global spray
    for x in range(n):
        for y in range(n):
            if spray[x][y] == now:
                spray[x][y] = 0
def isFinish():
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                return False
    return True
for now in range(1,m+1):
    if isFinish():# 나무가 모두 박멸되면 더이상 진행 X!!!!!
        break
    grow()
    spread()
    tx,ty = findSpot()# 가장 많이박멸되는 위치
    kill(tx,ty)
    removeSpray()# 제초제 제거.

print(answer)
    