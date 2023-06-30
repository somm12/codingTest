n,m = map(int,input().split())
r,c,d = map(int,input().split())

board= []
visited= [[0]*m for _ in range(n)]# 빈칸이지만,(벽이 아닌칸) 청소를 했는지 방문처리를 하기 위함.
cnt = 0
dx = [-1,0,1,0]# 북 동 남 서
dy = [0,1,0,-1]
for _ in range(n):
    board.append(list(map(int,input().split())))

def cleanNow():# 현재 칸이 아직 청소가 되지 않았다면 청소.
    global cnt, visited
    if visited[r][c] == 0: # 아직 방문 하지 않았다면, 로봇의 처음에 현재 위치 값은 빈칸임.
        cnt += 1
        visited[r][c] = 1
def isCleanNear():# 주변이 모두 이미 청소가 되었는가
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0<= ny <m:
            if visited[nx][ny] == 0 and board[nx][ny] == 0:# 방문처리가 X, 벽이 아닌 칸이 주변에 있다면
                return False # 청소가 안된칸이 있으므로 False 반환
    return True

def canBack():# 후진이 가능한지 체크
    global r,c 
    nx = r+ dx[(d+2)%4]# 현재 방향의 반대 방향=> 후진.
    ny = c + dy[(d+2)%4]
    if board[nx][ny] == 0: # 후진이 가능하다면, 뒤에 벽만 아니면 가능
        r = nx
        c = ny
        return True
    return False

def rotate90():# 반시계방향 90 회전
    global d
    d = (d-1)%4

def go():# 반시계 회전 이후, 해당 방향으로 앞칸이 청소 X칸이면 전진.
    global r,c
    nx = r+dx[d]
    ny = c+dy[d]
    if visited[nx][ny] == 0 and board[nx][ny] == 0:
        r = nx
        c = ny
        
while True:
    cleanNow() # 현재 칸 청소.

    if isCleanNear():# 주변 4칸이 모두 청소가 되었다면
        if canBack():# 후진 하기
            continue
        else: # 후진이 안되면 종료
            break
    else:
        rotate90() # 청소 안된칸이 있으면 반시계 90회전
        go() # 회전 후 앞칸이 청소가 X다면, 전진
print(cnt) # 청소한 칸 개수 출력
    