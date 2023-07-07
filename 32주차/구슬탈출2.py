from collections import deque
n,m = map(int,input().split())
board= []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by= i,j

def move():
    global rx,ry,bx,by
    q = deque()
    q.append((0,rx,ry,bx,by))
    visited = []
    visited.append((rx,ry,bx,by))
    while q:
        cnt, rx,ry,bx,by = q.popleft()
        if cnt > 10:
            return -1
        if board[rx][ry] =='O':
            return cnt
        for i in range(4):
            rnx = rx
            rny = ry
            while True:
                rnx += dx[i]
                rny += dy[i]
                if board[rnx][rny] == '#':
                    rnx -= dx[i]
                    rny -= dy[i]
                    break
                elif board[rnx][rny] == 'O':
                    break
            bnx = bx
            bny = by
            while True:
                bnx += dx[i]
                bny += dy[i]
                if board[bnx][bny] == '#':
                    bnx -= dx[i]
                    bny -= dy[i]
                    break
                elif board[bnx][bny] == 'O':
                    break
            if board[bnx][bny] == 'O':
                continue

            if rnx ==bnx and rny == bny:
                if abs(rnx-rx)+ abs(rny-ry) > abs(bnx-bx) + abs(bny-by):
                    rnx -= dx[i]
                    rny -= dy[i]
                else:
                    bnx -= dx[i]
                    bny -= dy[i]
            if not (rnx,rny,bnx,bny) in visited:
                q.append((cnt+1,rnx,rny,bnx,bny))
                visited.append((rnx,rny,bnx,bny))
    return -1
print(move())