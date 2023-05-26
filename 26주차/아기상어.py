from collections import deque
n = int(input())
g = []
sx, sy = 0,0
size = 2
time = 0
eaten = 0 # 먹은 것 개수를 담을 변수.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 9: # 상어 위치.
            sx = i
            sy = j

def bfs(a,b): # bfs를 통해 먹을 수 있는 물고기 후보를 고른다.(크기가 더 작고, 도달할 수 있는지.)
    q = deque()
    q.append((0,a,b)) 
    visited = [[0]*n for _ in range(n)]  
    visited[a][b] = 1
    cand = []
    while q:
        cnt, x, y= q.popleft()
        for i in range(4): # 인접한 4방향으로 탐색.
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if g[nx][ny] == size or g[nx][ny] == 0: # 지나갈 수만 있음.
                    visited[nx][ny] = 1
                    q.append((cnt+1,nx,ny))
                elif g[nx][ny] < size: # 물고기 크기가 더 작다면 먹을 수 있음. 후보로 추가.
                    visited[nx][ny] = 1
                    q.append((cnt+1,nx,ny))
                    cand.append((cnt+1,nx,ny))
    cand.sort(key=lambda x:(x[0],x[1],x[2])) # 거리가 가장 가깝고, 위쪽, 왼쪽 순으로 정렬.
    return cand
                    


while True:
    candidates = bfs(sx,sy)
    g[sx][sy] = 0 # 상어가 이동하므로 상어가 있던 자리는 빈칸이 됨.*** 
    if len(candidates) == 0: # 후보가 없다면, 즉 먹을 수 있는 물고기가 없으면 끝.
        break
    dist, row, col = candidates[0] # 젤 앞에 해당하는 후보를 먹기.
    time += dist # 한 칸 이동시 1초씩 걸리기 때문에, 거리가 곧 걸린 시간.
    sx,sy = row,col # 상어 위치 업데이트.
    g[row][col] = 0 # 먹이을 먹은 칸은 빈칸이 됨.
    eaten += 1 

    if size == eaten: # 아기 상어 크기가 먹은 물고기 수와 같은 때마다 크기 + 1 (때마다 => 다시 세기를 의미.)
        size += 1
        eaten = 0
print(time)
