from collections import deque
M,N,H = map(int,input().split())
tomato  = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int,input().split())))
    tomato.append(tmp)

answer = 0
dx = [-1,1,0,0] # 상하좌우 
dy = [0,0,-1,1]

q= deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                q.append((0,h,n,m))

def bfs():
    global tomato, answer

    while q:
        day,h,x,y = q.popleft()
        answer = max(answer,day)
        for i in range(4):# 상하좌우 방향
            nx = x +dx[i]
            ny = y +dy[i]
            if 0 <= nx < N and 0<= ny < M and tomato[h][nx][ny] == 0:
                tomato[h][nx][ny] =1
                q.append((day+1,h,nx,ny))
        for i in [1,-1]:# 수직 방향(앞뒤)
            nh = h+i
            if 0 <= nh < H and tomato[nh][x][y] == 0:
                tomato[nh][x][y] = 1
                q.append((day+1,nh,x,y))

def result():# 0이 남아있다면 -1(안익은 토마토가 남아있으면)
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 0:
                    return -1
    return answer

bfs()
print(result())
# 백준 BFS 토마토 문제