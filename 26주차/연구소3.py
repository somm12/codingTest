from collections import deque
n, m = map(int,input().split())
empty = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
v = []
answer = int(1e9)
g = []
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 0:
            empty += 1
        elif g[i][j] == 2:
            v.append((i,j))

def virus(arr):
    tmp = empty # 빈칸의 개수를 담은 변수.
    q = deque()
    visited = [[0]*n for _ in range(n)]
    for i,j in arr:
        visited[i][j] = 1 # bfs를 시작할 활성화 바이러스 위치는 방문처리.
        q.append((i,j,0)) # (i,j,걸리는 시간)
    while q:
        x,y, t = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if g[nx][ny] == 0 or g[nx][ny] == 2: # 비활성화 바이러스 or 빈칸이라면 활성화 바이러스로 변경
                    visited[nx][ny] = 1
                    q.append((nx,ny,t+1))
                    if g[nx][ny] == 0: # 빈칸을 만났을 때
                        tmp -= 1 # 빈칸 개수 줄어듦.
                        if tmp == 0: # 남은 빈칸이 0 이 된다면 바로 t+1 반환.
                            return t+1
    
    return int(1e9) # 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우.


def choose(L,res,start): # 활성화 바이러스 m개 선택.
    global answer
    if L == m:
        answer = min(answer, virus(res)) # 바이러스를 퍼뜨리고, 빈칸에 바이러스 퍼뜨리는데 걸리는 최소시간 update.
        return
    for i in range(start, len(v)):
        choose(L+1, res + [v[i]], i + 1)


if empty != 0: # 빈칸의 개수가 있다면 로직 수행..
    choose(0,[],0)
    if answer == int(1e9): # 모든 경우에서 전체 빈칸에 바이러스를 퍼뜨릴 수 없다면 -1반환.
        print(-1)
    else:
        print(answer)
else: # 빈칸이 없다면 이미 모든 칸이 벽, 바이러스이기 때문에 0출력.
    print(0)