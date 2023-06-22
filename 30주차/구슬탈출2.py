from collections import deque
n,m = map(int,input().split())
board = []

for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            x1,y1 = i,j
        elif board[i][j] == 'B':
            x2,y2 = i,j

dx= [-1,1,0,0]
dy = [0,0,-1,1]

def move():
    q = deque()
    q.append((1, x1,y1, x2,y2))
    visited = [(x1,y1,x2,y2)] # 이미 방문한 경우 대비
    while q:
        t,rx,ry,bx,by = q.popleft()
        if t > 10: # popleft를 했는데 t가 이미 10초를 넘는다면, 남은 q에도 모두 10보다 클 것. -1 반환.
            return -1
        for i in range(4): # 상 하 좌 우 방향 중 하나로 기울이기. ** 구슬 모두가 동시에 움직인다!
            rnx = rx + dx[i]
            rny = ry + dy[i]
            
            rnx = rx # 빨간 구슬이 구멍이나 벽을 만날때까지 움직이기.
            rny = ry
            while True:
                rnx += dx[i]
                rny += dy[i]
                if board[rnx][rny] == '#' or board[rnx][rny] == 'O':
                    break
            
            bnx = bx # 파란 구슬이 구멍이나 벽을 만날때까지 움직이기.
            bny = by
            while True:
                bnx += dx[i]
                bny += dy[i]
                if board[bnx][bny] == '#' or board[bnx][bny] == 'O':
                    break
            # 만약 파란 구슬이 구멍에 빠지면 실패이므로, 다른 경우 탐색.
            if board[bnx][bny] == 'O':
                continue
            # 빨간 구슬이 구멍에 빠지면 성공!
            elif board[rnx][rny] == 'O':
                return t
            # 모두 벽으로 이동했을 때, 멈추었므로, 한칸 뒤로.
            rnx -= dx[i]
            rny -= dy[i]
            bnx -= dx[i]
            bny -= dy[i]
            # 한 칸에 두 구슬이 동시에 있을 수 없기에, 더 먼거리에서 온 구슬이 한 칸 더 뒤로 간다.
            if rnx == bnx and rny == bny:
                if abs(rx-rnx) + abs(ry-rny) < abs(bx-bnx) + abs(by-bny):
                    bnx -= dx[i]
                    bny -= dy[i]
                else:
                    rnx -= dx[i]
                    rny -= dy[i]
            # 이미 방문했던 각 구슬의 좌표들은 다음에도 경우가 겹치므로, 방문처리로 표시.
            if (rnx,rny,bnx,bny) not in visited: 
                visited.append((rnx,rny,bnx,bny))
                q.append((t+1,rnx,rny,bnx,bny))
    return -1

                
print(move())

# BFS는 인접방향!으로, 이동하고 방문처리!를 해서, 최단거리로 갈 수 있는 방법을 찾는다.
