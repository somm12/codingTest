import copy
from collections import deque
n,m = map(int,input().split())

answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

g= []
cand = []
virus = []

for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if g[i][j] == 0:
            cand.append((i,j))# 벽이 될 수 있는 빈 칸을 후보 배열로 넣기
        elif g[i][j] == 2:
            virus.append((i,j))# 모든 바이러스가 퍼질 수 있도록 배열에 넣기.

def spread(arr):# 조합으로 벽 세개가 설치되면, bfs에 각 바이러스 좌표를 넣고 하나씩 인접한 방향으로 바이러스가 퍼진다.
    tmp = copy.deepcopy(g)
    q = deque()
    for x,y in arr:
        tmp[x][y] =1
    for x,y in virus:
        q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx,ny))
    area(tmp)

def area(tmp):# 빈칸 개수를 세어서 안전한 영역을 구하고, 최댓값을 위해 answer를 업데이트.
    global answer
    cnt =0 
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    answer = max(answer,cnt)
    
def install(L,res,start):
    if L == 3:
        spread(res)
        return
    
    for i in range(start, len(cand)):
        install(L+1, res+[cand[i]], i+1)

install(0,[],0)# 벽 3개 설치
print(answer)
# 이코테 bfs/dfs 문제