from collections import deque
n,m = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
g = []
answer = 0
for _ in range(n):
    g.append(list(map(int,input().split())))

def bfs(x,y,value,visited):# x,y를 시작으로 덩어리 만들기.
    visited[x][y]=1
    q =deque()
    q.append((x,y))
    one = []# 덩어리 좌표들을 모을 배열.
    redCnt =0
    reds = []# 빨간폭탄 좌표 담을 배열 => 이후에 다시 방문처리 0으로 수정.
    while q:
        
        x,y = q.popleft()
        one.append((x,y))
        if g[x][y] == 0:#빨간색이면 개수 세기
            redCnt +=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if g[nx][ny] == value or g[nx][ny] == 0:# 색이 같거나, 아니면 빨간 폭탄이거나.
                    visited[nx][ny] =1
                    q.append((nx,ny))
                    if g[nx][ny] == 0:# 빨간색은 공유가 가능하므로,, 이후에 방문 처리를 해야함.
                        reds.append((nx,ny))

    if len(one) < 2:# 2개이상이 아니면 덩어리 아님.
        return False

    one.sort(key=lambda x:(-x[0],x[1]))# 기준점 찾기
    for i,j in one:
        if g[i][j] != 0:
            mx,my = i,j
            break
    for i,j in reds:# 빨간 폭탄은 다음에 다시 다른 폭탄과 함께 묶음이 될 수 있으므로, 다시 방문처리를 0으로 하기.
        visited[i][j] = 0
    return [len(one), redCnt, mx,my, one]# 총 개수, 빨간 폭탄개수, 기준점x,기준점y, 한 묶음 모든 좌표 배열. 

def remove(arr):# 제거하기.
    global g
    for x,y in arr:
        g[x][y] = '#'
def gravity():# 중력 발생!! 돌은 중렬 작용안함.
    global g
    for j in range(n):
        for _ in range(n):
            for i in range(n-2,-1,-1):
                if g[i][j] != '#' and g[i][j] >= 0:
                    if g[i+1][j] == '#':
                        g[i+1][j], g[i][j] = g[i][j], g[i+1][j]
def rotate():# 반시계 90 회전.
    global g
    newG = [['#']*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            newG[n-1-y][x] = g[x][y]
    g = newG

def findBig():# 제일 큰 덩어리 찾기.

    cand = []
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if g[x][y] != '#' and 1 <= g[x][y] <= m and not visited[x][y]:
                tmp = bfs(x,y,g[x][y], visited)
                if tmp != False:
                    cand.append(tmp)
    if len(cand) == 0:
        return False
    cand.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))# 개수 많고 > 빨간 폭탄 적고 > 기준점 행이 크고 > 기준점 열이 작은 순.

    return cand[0][4]# 가장 큰 덩어리 좌표 배열 반환

while True:
    arr = findBig()
    if arr == False:# 더이상 묶음 없으면 종료.
        break
    answer += (len(arr)**2)# 점수 획득.
    remove(arr)


    gravity()
    rotate()
    gravity()


print(answer)
# 삼성 기출.
# 빨간 폭탄 관련 조건 유의 + 빨간 폭탄 방문처리 유의