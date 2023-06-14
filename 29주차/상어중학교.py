from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int,input().split())
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

answer = 0

def bfs(a,b): # 하나의 좌표를 중심으로 한 그룹을 만든다.
    q = deque()
    arr = [] # 좌표
    rainbow = 0 # 무지개 블록 개수
    q.append((a,b))
    visited = [[0]*n for _ in range(n)]
    visited[a][b] = 1
    normal = 0 # 일반 블록 적어도 한개는 필요
    color = 0 # 일반 블록들의 색은 모두 같아야함.
    flag = True # 일반 블록의 색을 통일 시키기 위한. 색을 담을 변수
    while q:
        x,y = q.popleft()
        arr.append((x,y))
        if board[x][y] == 0: # 무지개 블록 수 세기
            rainbow += 1
        elif 1<= board[x][y] <= m: # 첫 일반 블록일 경우
            if flag: # 색을 저장.
                color = board[x][y]
                flag = False
            normal += 1 # 일반 블록 개수 세기
         
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            # 범위 내, 방문 안했으며,빈칸도 아니며(-2),검은색도 아닌 블록 중에서
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1 and board[nx][ny] != -2 and  not visited[nx][ny]:
                if board[nx][ny] == 0: # 무지개 블록은 있든 말든 상관 없음.
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == color or flag == True: # 같은 블록 색이거나 첫 일반 블록일 때, 색 저장.
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    flag = False
                    color = board[nx][ny]
    
    if normal >= 1 and len(arr) >= 2: # 그룹은 일반블록이 1개, 총 2개 이상 만들어 져야함
        s = [] # 그룹의 기준점 구하기
        for x,y in arr: 
            if board[x][y] != 0: # 검은색 블록이 아닌 것 중에서 가장 행과 열이 작은 것.
                s.append((x,y))
        s.sort(key = lambda x: (x[0],x[1]))
        
        
        return [rainbow, s[0],arr] # [무지개 개수, 기준점, 그룹 내 블록 좌표]
        
    return []

def find():
    cand = []
    for x in range(n):
        for y in range(n):
            if board[x][y] != -1 and board[x][y] != -2:
                tmp = bfs(x,y)
                if len(tmp) > 0:
                    cand.append(tmp)
    # 가장 개수가 많고 > 무지개 블록 개수 > 기준점 행이 크고 > 기준점 열이 큼. 우선순위로 큰 그룹 뽑기.
    cand.sort(key=lambda x : (-len(x[2]),-x[0], -x[1][0], -x[1][1]))
    if len(cand) > 0: # 그룹의 x,y 좌표 반환.
        return cand[0][2]
    return []# 만약 어떤 그룹도 생기지 못한다면

def remove(g): # 그룹 블록 다 제거
    global board
    for x,y in g:
        board[x][y] = -2
    
def gravity(): # 중력: 검은색 블록 뻬고! 나머지 블록 모두 큰 행 쪽으로 이동.
    global board
  
    for x in range(n-1,-1,-1):
        for y in range(n):
            if board[x][y] != -2 and board[x][y] != -1: # 빈칸, 검은색 블록 제외
                nx = x
                ny = y
                while True: 
                    nx += dx[1]
                    if not (0 <= nx < n) or board[nx][ny] != -2:
                        break
                nx -= dx[1] # break 되었으니 다시 한 칸 위쪽으로.
                tmp = board[x][y]
                board[x][y] = -2
                board[nx][ny] = tmp # 빈칸으로 채우고, 이동할 칸에 값을 담는다.
    

def rotate(): # 반시계 90 회전. 
    global board
    new = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            new[n-1-y][x] = board[x][y]
    board = new
                    
while True: 
    big = find() # 가장 큰 그룹 찾기
    if len(big) <= 1: # 블록 개수가 1개 이하면 끝.
        break
    remove(big) # 블록 다 제거.
    answer += len(big)**2 # 블록 개수의 제곱 수만큼 획득
    gravity() # 중력 작용. 
    rotate() # 반시계 90 회전
    gravity() # 중력 작용
print(answer)