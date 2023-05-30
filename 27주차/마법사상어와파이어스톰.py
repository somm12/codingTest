from collections import deque
n,Q = map(int,input().split())
ice = []
arr = [] # L 담을 배열
dx = [-1,1,0,0]
dy = [0,0,-1,1]
LEN = 2**n
for _ in range(LEN):
    ice.append(list(map(int,input().split())))

arr = list(map(int,input().split()))


def rotate(L): # 부분 격자 회전 함수. 
    global ice
    new = [[0]*LEN for _ in range(LEN)]
    for i in range(0,LEN, 2**L): 
        for j in range(0,LEN, 2**L):
            # 2^L x 2^L 부분 격자 회전 결과만 담기 위한 배열 arr.
            arr = []
            for x in range(i, i+2**L):
                a = []
                for y in range(j,j + 2**L):
                    a.append(ice[x][y])
                arr.append(a)
            # 시계방향 90도 회전.
            tmp = [[0]*len(arr) for _ in range(len(arr))]
            for x in range(2**L):
                for y in range(2**L):
                    tmp[y][2**L-1-x] = arr[x][y]
            
            # 현재 부분 격자 부분에 회전 결과 할당
            for x in range(2**L):
                for y in range(2**L):
                    new[x+i][y+j] = tmp[x][y]
            
            
    # 바뀐 부분 할당.
    ice = new
    
    

def reduce(): # 인접한 칸 주변에 얼음이 있는 칸이 3개이상이 아니면 얼음양 -1
    global ice
    new = [[0]*LEN for _ in range(LEN)] # 새로운 배열을 할당해서 얼음양 줄인 결과를 담음.**
    
    for i in range(LEN):
        for j in range(LEN):
            cnt = 0 # 얼음 있는 칸이 몇 칸인지 세기
            if ice[i][j] > 0:
                for k in range(4): # 인접한 상하좌우
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < LEN and 0 <= ny < LEN and ice[nx][ny] > 0:
                        cnt += 1
                
                if cnt <= 2:
                    new[i][j] = ice[i][j] - 1 
                else:
                    new[i][j] = ice[i][j]
    ice = new
    

def bfs(x,y): # 가장 큰 얼음 덩어리를 이루는 칸 개수 구하기. 인접한 칸에 얼음이 존재하면 연결되어있음.
    global check
    q = deque()
    q.append((x,y))
    check[x][y] = 1
    cnt = 0 # 얼음이 있는 칸이 한 덩어리에 몇 개있는가 체크
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < LEN and 0 <= ny < LEN and not check[nx][ny]:
                if ice[nx][ny] > 0: # 인접한 부분에 얼음이 있다면
                    check[nx][ny] = 1
                    q.append((nx,ny))
    return cnt


for i in range(Q):
    rotate(arr[i])
    reduce()

total = 0
big = 0 # 덩어리가 없다면 ( 얼음 있는 칸이 없다면. ) 0 출력.

for i in range(LEN):
    for j in range(LEN):
        total += ice[i][j]

check = [[0]*LEN for _ in range(LEN)]
for i in range(LEN):
    for j in range(LEN):
        if not check[i][j] and ice[i][j] > 0:
            big = max(big, bfs(i,j)) # 최대 얼음칸 개수 할당.

print(total)
print(big)


  