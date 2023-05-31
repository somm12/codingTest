from collections import deque
dx = [0,1,0,-1] # 동 남 서 북. (시계방향)
dy = [1,0,-1,0]
total = 0
dice = [1,2,3,4,5,6] # dice[5]가 아랫면
direction = 0 # 주사위가 향하는 방향. 처음은 동쪽
lx, ly = 0,0 # 현재 주사위 위치.

n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

def move():
    global direction, dice, lx, ly
    
    nx = lx + dx[direction]
    ny = ly + dy[direction]
    if 0 <= nx < n and 0 <= ny < m: # 다음칸으로 이동할 수 있으면
        lx = nx
        ly = ny
    else: # 아니면 반대방향으로 이동
        direction += 2
        direction = direction % 4
        lx += dx[direction]
        ly += dy[direction]
    # 전개도 변경.
    a,b,c,d,e,f = dice
    if direction == 0: # 동쪽 
        dice = [d,b,a,f,e,c]
    elif direction == 1: # 남쪽
        dice = [b,f,c,d,a,e]
    elif direction == 2: # 서쪽
        dice = [c,b,f,a,e,d]

    elif direction== 3: # 북쪽
        dice = [e,a,c,d,f,b]
    
    
def score():
    global total

    B = g[lx][ly]
    q = deque()
    q.append((lx,ly))
    C = 0
    visited = [[0]*m for _ in range(n)]
    visited[lx][ly] = 1
    while q:
        x,y = q.popleft()
        C += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if g[nx][ny] == B:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    total += (B*C)
def rotate():
    global direction
    A = dice[5]
    B = g[lx][ly]
    
    if A > B:
        
        direction += 1
        direction = direction%4
        
    elif A < B:
        direction -= 1
        direction = direction% 4
for i in range(1,k+1): # k번 이동.

    move() # 주사위 이동
    score() # 점수 얻기
    rotate() # 이동 방향 바꾸기
  

print(total) # 각 이동때마다 얻은 점수의 합.