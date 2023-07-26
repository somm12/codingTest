from collections import deque
import copy
dx = [-1,1,0,0]# 상 하 좌 우
dy = [0,0,-1,1]

n,Q = map(int,input().split()) # Q번 시전
g = []
for _ in range(2**n):
    g.append(list(map(int,input().split()))) # 2^n x 2^n 배열.

arr = list(map(int,input().split()))

def rotate(L):# 부분격자 회전하기.
    global g
    new = [[0]*(2**n) for _ in range(2**n)]
    for x in range(0,2**n,2**L): # 시작점 (x,y)
        for y in range(0,2**n, 2**L):

            for i in range(2**L): # 시작점으로 부터 2^L 만큼 떨어진 격자
                for j in range(2**L):
                    new[x+j][y+ 2**L-1-i] = g[x+i][y+j]# 새로운 배열에 회전 시킨 내용을 할당.

    g=  new# 바뀐 배열 다시 재할당


def reduceIce():# 얼음 양 줄이기.
    global g
    new = copy.deepcopy(g)# 배열을 복사해서, 원래 배열 g를 참고하여, 확인하고 복사한 배열에 얼음양을 줄이기
    for x in range(2**n):
        for y in range(2**n):
            if g[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < 2**n and 0 <= ny < 2**n:
                        if g[nx][ny] > 0:
                            cnt += 1
                if cnt < 3:
                    new[x][y] -= 1
    g = new# 얼음양을 줄인 상타를 다시 재할당.

for L in arr:# Q번 시전
    rotate(L)# 부분격자 회전
    reduceIce()# 얼음양 줄이기
   

total = 0
for i in range(2**n):# 총 남은 얼음양
    for j in range(2**n):
        total += g[i][j]

def bfs(x,y): # 최대 얼음 덩어리 구하기. bfs로 상하좌우로 면적을 넓혀나가기
    global visited
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 아직 방문하지 않은 얼음 중에서, 얼음양이 1이상인지 체크.
            if 0 <= nx < 2**n and 0 <= ny < 2**n and not visited[nx][ny] and g[nx][ny] > 0:
                q.append((nx,ny))
                cnt += 1
                visited[nx][ny] = 1
    return cnt


# 최대 얼음 덩어리 개수 
bigCnt =0
visited = [[0]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if g[i][j] > 0 and not visited[i][j]:
            bigCnt = max(bigCnt,bfs(i,j))
print(total)
print(bigCnt)