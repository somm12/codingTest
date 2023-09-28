from collections import deque

n,q = map(int,input().split())
N = (2**n)
ice = []
for _ in range(N):
    ice.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
answer = 0
group = [] # 빙하 덩어리 개수를 담을 배열
dx = [-1,1,0,0]# 상하좌우 인접 접근을 위한 dx,dy
dy = [0,0,-1,1]


def rotate():# 회전하기 : 2^L x 2^L 내에서, 2^(L-1) x 2^(L-1) 씩 4조각 나눠서 시계방향 회전.
    global ice
    m = (2**L)
    k = (2**(L-1))
    tmp = [[0]*N for _ in range(N)]
    for x in range(0,N,m):# 선택되는 범위에서 가장 좌측상단 좌표인 x,y
        for y in range(0,N,m):

            for i in range(m):# x,y 좌표를 시작으로,2^(L-1) x 2^(L-1) 씩 4조각 나눠서 시계방향 회전.
                for j in range(m):

                    value = ice[x+i][y+j]
                    if i < k and j < k:# 좌측 상단의 (2^L-1 x 2^L-1) 부분은 오른쪽으로 k만큼 이동
                        tmp[x+ i][y+ j+k] = value
                    elif i<k and j >=k:# 오른쪽 상단은 아래로 이동.
                        tmp[x+ i+k][y+j] = value
                    elif i >= k and j >= k:# 우측하단 부분은 왼쪽이동
                        tmp[x+ i][y+j-k] = value
                    elif i >= k and j < k:# 좌측하단은 위로 이동.
                        tmp[x+ i-k][y+j] = value
    ice = tmp #이동한 부분 업데이트.

def melting():# 동시에 인접한 칸 중, 얼음이 있는 칸이 3개이상이면 녹지 않고 아니면 -1.
    global ice
    tmp = [a[:] for a in ice]# ice배열 복사.
    for x in range(N):
        for y in range(N):
            if ice[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x+ dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and ice[nx][ny] > 0:
                        cnt += 1
                if cnt >= 3:
                    continue
                else: tmp[x][y] -=1
    ice = tmp
def bfs(x,y):# 가장 큰 빙하 덩어리 개수를 구하기 위한 함수.
    global visited
    q= deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 0

    while q:
        x,y = q.popleft()
        cnt += 1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and ice[nx][ny] >0 :
                q.append((nx,ny))

                visited[nx][ny] =1

    return cnt

for L in arr:
    if L >0:# L이 0이면, 그대로
        rotate()
    melting()

for x in range(N):
    for y in range(N):
        answer += ice[x][y]

if answer > 0:
    visited = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if not visited[a][b] and ice[a][b] >0 :
                group.append(bfs(a,b))
    print(answer)
    print(max(group))
else:#얼음이 없다면 빙하 덩어리도 없으므로, 0을 출력.
    print(0)
    print(0)
# 삼성 기출 코드트리.