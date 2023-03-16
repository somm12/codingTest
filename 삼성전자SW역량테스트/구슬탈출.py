from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
g = []
for i in range(n):
    g.append(list(input()))
    for j in range(len(g[i])):
        if g[i][j] == 'R':
            rx,ry = i,j
        elif g[i][j] == 'B':
            bx,by = i,j
def bfs(rx,ry,bx,by):
    visited = []
    cnt = 0
    q = deque()
    q.append((rx,ry,bx,by,cnt))
    visited.append((rx,ry,bx,by))
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10:
            print(0)
            return 
        if g[rx][ry] == 'O':
            print(1)
            return
        for i in range(4):
            nrx = rx
            nry = ry
            while True:
                nrx += dx[i]
                nry += dy[i]
                if g[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                if g[nrx][nry] == 'O':
                    break
            nbx = bx
            nby = by
            while True:
                nbx += dx[i]
                nby += dy[i]
                if g[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                if g[nbx][nby] == 'O':
                    break
            if g[nbx][nby] == 'O':
                continue
            if nrx == nbx and nry == nby:
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx-bx) + abs(nby-by):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not (nrx,nry,nbx,nby) in visited:
                visited.append((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,cnt+1))
    print(0)
    return
bfs(rx,ry,bx,by)
