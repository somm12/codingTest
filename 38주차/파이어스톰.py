import copy
from collections import deque
n,Q = map(int,input().split())

ice = []
N = 2 ** n
for _ in range(N):
    ice.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

arr = list(map(int,input().split()))


def divideAndRotate():
    global ice,L
    length = 2**L
  
    new = [[0]*(2**n) for _ in range(2**n)]
    for i in range(0,N,length):
        for j in range(0,N,length):
            for x in range(length):
                for y in range(length):

                    new[i+y][j+length-1-x] = ice[i+x][j+y]
    ice = new      
def reduceIce():
    global ice
    new = copy.deepcopy(ice)
    for x in range(N):
        for y in range(N):
            cnt = 0
            if ice[x][y] > 0:
                for i in range(4):
                    nx = x +dx[i]
                    ny = y+dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if ice[nx][ny] > 0:
                            cnt += 1
                if cnt < 3:
                    new[x][y] -= 1
    ice = new

def biggestCnt(x,y):
    global visited, total
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx= x+ dx[i]
            ny = y +dy[i]
            if 0 <= nx < N and 0 <= ny <N and not visited[nx][ny]:
                if ice[nx][ny] > 0:# 얼음이 있는 칸 중에서!
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    cnt += 1
    return cnt
                    

  
            
for L in arr:
    divideAndRotate()# 부분격자 회전
 
    reduceIce()# 인접한 얼음이 3개 미만이라면, 얼음 양 -1

answer =0 
for i in ice:
    answer += sum(i) # 총 얼음양

visited = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        total = 0
        if not visited[i][j] and ice[i][j] > 0:
            cnt = max(cnt,  biggestCnt(i,j)) # 가장 큰 얼음덩어리의 얼음개수.
print(answer)
print(cnt)
    