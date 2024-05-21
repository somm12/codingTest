from collections import deque

n,m = map(int,input().split())
g = []
visited = {}
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    g.append(list(input()))
    for j in range(m):
        if g[i][j] == 'R':
            rx,ry = i,j
        elif g[i][j] == 'B':
            bx,by = i,j
visited[(rx,ry,bx,by)] =1
q.append((rx,ry,bx,by,0))
cnt = 0

flag = False

while q:
    rx,ry,bx,by,cnt = q.popleft()
    if cnt >= 10:# 이미 cnt 번까지 기울이기 시행했음. 가능10번 이하로도 안되면. 멈추기.
        break
    for i in range(4):
        nrx, nry = rx,ry
        while True:# 빨간 구슬 이동.
            nrx += dx[i]
            nry += dy[i]
            if g[nrx][nry] == '#' or g[nrx][nry] == 'O':
                break
        nbx, nby = bx,by
        while True:# 파란 구슬 이동.
            nbx += dx[i]
            nby += dy[i]
            if g[nbx][nby] == '#' or g[nbx][nby] == 'O':
                break
        if g[nbx][nby] == 'O': continue# 파란구슬은 빠지면 안됨.
        if g[nrx][nry] == 'O':# 빨간 구슬은 빠지면 바로 종료.
            flag = True
            break
        nrx -= dx[i]
        nry -= dy[i]
        nbx -= dx[i]
        nby -= dy[i]
        if nrx == nbx and nry == nby:# 같은 칸에 있다면, 더 먼곳에서 온걸 반대방향 한 칸 더 이동.
            r = abs(nrx-rx) + abs(nry-ry)
            b = abs(nbx-bx) + abs(nby-by)
            if r > b:# 빨간 구슬이 늦게 움직임.
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]
        
        if (nrx,nry,nbx,nby) not in visited:# 다음 경우 추가.
            visited[(nrx,nry,nbx,nby)] = 1
            q.append((nrx,nry,nbx,nby,cnt+1))
    if flag:# 구멍에 빠진 경우.
        print(cnt+1)
        break

if not flag:# 10번이 넘거나 안되는 경우.
    print(-1)
