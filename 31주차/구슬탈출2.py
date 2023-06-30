from collections import deque
n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move():
    global rx,ry,bx,by
    q = deque()
    q.append((rx,ry,bx,by,0)) # 빨간구슬 파란구슬, 현재 몇번 기울였는지 cnt append
    visited = []
    visited.append((rx,ry,bx,by))

    while q:
        rx,ry, bx,by, cnt = q.popleft()
        if cnt > 10:# 만약 10번 이하로 기울여도 안되면 -1 반환.
            return -1
        if board[rx][ry] == 'O': # 빨간구슬이 구멍에 빠졌다면 cnt반환.
            return cnt
        for i in range(4):# 상하 좌우 중 한 방향으로 움직이기.
            rnx = rx
            rny = ry
            while True: # 빨간구슬 움직이기
                rnx += dx[i]
                rny += dy[i]
                if board[rnx][rny] == '#': # 벽을 만난다면, 그 전 좌표로 옮기기
                    rnx -= dx[i]
                    rny -= dy[i]
                    break
                elif board[rnx][rny] == 'O':# 구멍을 만나면 멈춘다.
                    break
            
            bnx = bx
            bny = by
            while True:# 파란 구슬 움직이기
                bnx += dx[i]
                bny += dy[i]
                if board[bnx][bny] == '#': # 벽을 만난다면, 그 전 좌표로 한칸 옮기기
                    bnx -= dx[i]
                    bny -= dy[i]
                    break
                elif board[bnx][bny] == 'O':# 구멍 만나면 멈추기.
                    break

            if board[bnx][bny] == 'O':# 만약 파란 구슬이 구멍에 빠진다면(둘다 동시에 빠진 경우, 파란구슬만 빠진 경우 모두) 이 경우는 pass. 
                continue

            if rnx == bnx and rny == bny:# 두 구슬은 동시에 같은 칸에 있을 수 없으므로, 더 멀리서 움직인 칸이 한 칸 더 뒤로.
                a = abs(rx-rnx) + abs(ry-rny)
                b = abs(bx-bnx) + abs(by-bny)
                if a > b:
                    rnx -= dx[i]
                    rny -= dy[i]
                else:
                    bnx -= dx[i]
                    bny -= dy[i]
            
            if (rnx,rny,bnx,bny) not in visited:# 이미 방문 했던 좌표가 아닐 때, q에 추가, 방문처리해주기.
                q.append((rnx,rny,bnx,bny,cnt+1))
                visited.append((rnx,rny,bnx,bny))
    return -1

print(move())
# return 을 하는 함수라면 꼭 while문 바깥에도 return을 써야함.
