from collections import deque
n,m = map(int,input().split())
g  =[]
for i in range(n):
    g.append(list(input()))
    for j in range(m):
        if g[i][j] == 'R':
            rx,ry = i,j
        elif g[i][j] == 'B':
            bx,by = i,j
dx =[ -1,1,0,0]
dy = [0,0,-1,1]

def bfs(rx,ry,bx,by):
    q= deque()
    q.append((rx,ry,bx,by,0))
    visited = set()# 빨간 구슬, 파란 구슬 위치를 저장해서 같은 경우가 나오지 않게 set 사용.
    visited.add((rx,ry,bx,by))
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt >= 10:continue#이미 10번 기울이기 했으므로, 넘기기. => 10번 이하로 안되면 -1
        for i in range(4):
            nrx,nry = rx,ry
            while True:
                nrx += dx[i]
                nry += dy[i]
                if g[nrx][nry] == '#' or g[nrx][nry] == 'O':
                    break
            nbx,nby = bx,by
            while True:
                nbx += dx[i]
                nby += dy[i]
                if g[nbx][nby] == '#' or g[nbx][nby] == 'O':
                    break
            
            if g[nbx][nby] == 'O':continue # 파란 구슬은 구멍에 빠지면 안됨.
            if g[nrx][nry] == 'O': # 빨간 구슬만 구멍에 빠진 다면 바로 종료.
                return cnt +1
            nrx -= dx[i]# 벽에 도착했으므로, 한칸 뒤로
            nry -= dy[i]
            nbx -= dx[i]
            nby -= dy[i]
            if nrx == nbx and nry == nby:
                if abs(nrx-rx)+abs(nry-ry) < abs(nbx-bx)+abs(nby-by):# 한 칸에 구슬이 동시에 존재할 수 없기 때문에, 더 먼 곳에서 온 구슬이 더 뒤로.
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]
            if (nrx,nry,nbx,nby) not in visited:# 이미 같은 경우가 없다면 큐에 추가.
                q.append((nrx,nry,nbx,nby,cnt+1))
                visited.add((nrx,nry,nbx,nby))
    return -1

print(bfs(rx,ry,bx,by))
# 백준 구슬 탈출2.