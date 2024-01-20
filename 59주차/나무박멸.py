n,m,k,c = map(int,input().split())
answer = 0
tree = []
kill = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [ 0,0,-1,1]

kx = [-1,1,1,-1]
ky = [1,1,-1,-1]

def inRange(x,y):
    return 0 <= x < n and 0<= y < n

def grow():# 나무 성장.
    global tree
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if inRange(nx,ny) and tree[nx][ny] > 0:
                        cnt += 1
                tree[x][y] += cnt

def sprayGone():# 유효기간 지난 제초제 처리
    global kill
    for x in range(n):
        for y in range(n):
            if kill[x][y] > 0 and kill[x][y] < year:
                kill[x][y] = 0

def spread():#나무 번식
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
                    if inRange(nx,ny) and tree[nx][ny] == 0 and kill[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:
                    value = tree[x][y] // cnt
                    for i in range(4):
                        nx,ny = x+dx[i],y+dy[i]
                        if inRange(nx,ny) and tree[nx][ny] == 0 and kill[nx][ny] == 0:
                            tmp[nx][ny] += value

    tree = tmp

def findPlace():# 제초제를 뿌렸을 때, 가장 박멸이 많이 되는 칸 찾기 (빈칸이나 벽나오면 멈추기)
    cand = []
    for x in range(n):
        for y in range(n):
            if tree[x][y] > 0:
                cnt = tree[x][y]
                for i in range(4):
                    for j in range(1,k+1):
                        nx,ny = x+(kx[i]*j), y+(ky[i]*j)
                        if not inRange(nx,ny):
                            break
                        if tree[nx][ny] > 0:
                            cnt += tree[nx][ny]
                        else:# 벽이나 빈칸이라면
                            break
                cand.append((cnt,x,y))
    if len(cand) >0:
        cand.sort(key=lambda x:(-x[0],x[1],x[2]))
        return cand[0]

    return [0,-1,-1]

def spray():# 제초제 처리.
    global answer,tree, kill
    num,x,y = findPlace()
    
    answer+= num
    if num > 0:
        tree[x][y] = 0
        kill[x][y] = year+c
        for i in range(4):
            for j in range(1,k+1):
                nx,ny = x+(kx[i]*j), y+(ky[i]*j)
                if not inRange(nx,ny):
                    break
                if tree[nx][ny] > 0:
                    tree[nx][ny] = 0
                    kill[nx][ny] = year+c# 현재 년수 + c년까지 유지.
                else:# 벽이나 빈칸이라면
                    kill[nx][ny] = year+c
                    break
    
            
for _ in range(n):
    tree.append(list(map(int,input().split())))
for year in range(1,m+1):
    grow()
    sprayGone()
    spread()
    spray()
    

print(answer)