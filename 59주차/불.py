from collections import deque
tc = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def inRange(w,h, x,y):
    return 0<= x < h and 0 <= y < w

def bfs():
    time = 0
    while q:# 불이 이동하려는 곳과 불이 있는 칸은 피해야하므로, 불을 먼저 이동시킴.
        while fire and fire[0][0] <= time:
            t,x,y = fire.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if inRange(w,h,nx,ny) and g[nx][ny] != '#' and g[nx][ny] != '*':
                    g[nx][ny] = '*'
                    fire.append((t+1,nx,ny))

        while q and q[0][0] <= time:
            t,x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if not inRange(w,h,nx,ny):
                    return t+1
                if g[nx][ny] == '.':
                    g[nx][ny] = '@'
                    q.append((t+1,nx,ny))
        time += 1
        
    return 'IMPOSSIBLE'

for _ in range(tc):
    w,h = map(int,input().split())
    g = []
    q = deque()
    fire = deque()
    for i in range(h):
        g.append(list(input()))
        for j in range(w):
            if g[i][j] == '@':
                q.append((0,i,j))
            elif g[i][j] =='*':
                fire.append((0,i,j))
    print(bfs())
