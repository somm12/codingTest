import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def inRange(x,y):
    return 0 <= x < h and 0 <= y < w
def bfs():
    count = 0
    while q:# 상근이가 탈출할 때 까지
        count += 1
        while fire and fire[0][2] < count:# 불이 먼저 이동. 다음 초 전까지 불만 이동.
            x,y,time= fire.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if g[nx][ny] == '.' or g[nx][ny] == '@':
                        visited[nx][ny] =1
                        g[nx][ny] = '*'
                        fire.append((nx,ny,time+1))
       
        # 상근 이동
        while q and q[0][2] < count: #다음 초 전까지 위치만 이동.
            x,y,time= q.popleft()
            if x == 0 or x == h-1 or y == 0 or y == w-1:# 테두리에 도달하면 탈출.
                return count
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if g[nx][ny] == '.':
                        visited[nx][ny]=1
                        q.append((nx,ny,time+1))
       
       
                       
        
    return 'IMPOSSIBLE'
            
    
for _ in range(tc):
    w,h = map(int,input().split())
    fire = deque()# 불의 이동 위치를 담음
    q = deque()# 상근의 이동 위치들을 담음
    g = []
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        g.append(list(input().rstrip()))
        for j in range(w):
            if g[i][j] == '*':# 불 위치, 현재까지의 초수
                fire.append((i,j,0))
            elif g[i][j] == '@':
                visited[i][j] =1
                q.append((i,j,0))# 상근이 위치
    print(bfs())
# 백준 .