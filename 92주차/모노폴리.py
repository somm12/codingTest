n,m,k =map(int,input().split())
g = [[[] for _ in range(n)] for _ in range(n)]# 계약땅 정보
board = [[[] for _ in range(n)] for _ in range(n)]# 현재 위치 정보

locat = {}
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j] > 0:
            g[i][j] = [arr[j],k]
            locat[arr[j]] = [i,j]
arr = list(map(int,input().split()))
for i in range(m):
    locat[i+1].append(arr[i]-1)
    x,y = locat[i+1][0],locat[i+1][1]
    board[x][y].append([i+1,arr[i]-1])
p = [[] for _ in range(m+1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(1,m+1):
    for _ in range(4):
        arr = list(map(int,input().split()))
        tmp =[]
        for v in arr:
            tmp.append(v-1)
        p[i].append(tmp)


def inRange(x,y):
    return 0 <= x < n and 0 <=y < n

def isFinish():
    if len(locat) == 1:
        return True
    return False

def move():
    global locat,board
    tmp = {}
    for num in locat:
        x,y,di = locat[num]
        flag = False
        for nd in p[num][di]:# 우선순위 대로 이동!! 만약 빈 땅이라면 이동바로하기.
            nx,ny = x+dx[nd],y + dy[nd]
            if inRange(nx,ny) and len(g[nx][ny])==0:
                flag= True
                tmp[num] = [nx,ny,nd]
                board[x][y] = []
                board[nx][ny].append([num,nd])
                break

        if not flag:
            for nd in p[num][di]:# 빈 땅이 없다면 자기 땅으로 이동.
                nx,ny = x+dx[nd],y + dy[nd]
                if inRange(nx,ny) and len(g[nx][ny]) > 0 and g[nx][ny][0] == num:
                    tmp[num] = [nx,ny,nd]
                    board[x][y] = []
                    board[nx][ny].append([num,nd])
                    break

    locat = tmp

def check():
    global g, locat,board
    for x in range(n):
        for y in range(n):
            if len(board[x][y]) > 1:
                board[x][y].sort(key= lambda x : x[0])# 이동 후, 여러 사람이 있다면, 작은 번호 제외하고 사라짐.
                number,direct = board[x][y][0]
                for num, di in board[x][y][1:]:
                    del locat[num]
                board[x][y] = [[number,direct]]
                g[x][y] = [number,k] # 독점 계약후. 표시
    for num in locat:# 독점 계약 후 표시.
        x,y,di = locat[num]
        g[x][y] = [num,k]
def period():# 기간 -1
    global g
    for x in range(n):
        for y in range(n):
            if len(g[x][y]) > 0:
                g[x][y][1] -= 1
                if g[x][y][1] == 0:
                    g[x][y] = []


time = 0
while True:
    if time >= 1000:
        print(-1)
        break
    if isFinish():
        print(time)
        break

    move()
    period()
    check()

    time += 1
# 코드트리 승자독식 모노폴리
# 1.각 방향마다 우선순위 대로 이동. 2. 독점 유효기간 유지는 이동 이후에 처리.