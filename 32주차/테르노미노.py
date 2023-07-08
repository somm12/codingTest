n,m = map(int,input().split())
answer = -1
board = []

dx = [-1,1,0,0] # 상하 좌우.
dy = [0,0,-1,1]
maxV = -1
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        maxV = max(maxV,board[i][j]) # 최대 값을 구해놓기.

def makeIt(L,x,y,total):
    global visited, answer
    if total + (4-L)*maxV <= answer: # 현재 total에서 최대값을 구해도 answer이하면 굳이 더 찾지 않기.
        return
    if L == 4: # 4개 테르노미노 만들어지면 stop
        answer = max(answer,total)
        return
    for i in range(4): # 상하좌우 중 한 방향으로 뻗어나가기.
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if L == 2: # 두번째 블록일때,ㅏ 모양을 대비해서, 다음 좌표를 매개변수를 넘기지 않는다.
                visited[nx][ny] = 1
                makeIt(L+1,x,y,total + board[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1 # ㅏ 형태가 아닌 경우도 수행!.
            makeIt(L+1,nx,ny,total + board[nx][ny]) # 다음 위치 좌표를 넘기면서 다음 위치에서 상하좌우 중 한 방향으로 테르노미노를 만들어나감.
            visited[nx][ny] = 0
            
                

visited = [[0]*m for _ in range(n)] # 이미 방문한 칸을 처리하기 위함.
for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        makeIt(1,x,y,board[x][y])# 시작점은 이미 방문 처리하고, 이어나가기.
        visited[x][y] = 0
print(answer)