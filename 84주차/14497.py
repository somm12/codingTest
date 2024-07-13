from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
x1 -=1
y1 -=1
x2 -=1
y2 -= 1
g = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    g.append(list(input().rstrip()))

def inRange(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(x,y):
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    q= deque()
    
    q.append((x,y))
    turn = 0
    while g[x2][y2] != '0': # 0으로 할당 되기 전까지 반복.
        turn += 1
        loop = deque()# 다음 턴에서 퍼지는 큐.
        while q:# 현재 큐에서 퍼짐.
            x,y = q.popleft()
            for i in range(4):# 4방향으로 퍼짐.
                nx,ny = x+dx[i],y+dy[i]
                if inRange(nx,ny) and not visited[nx][ny]:
                    visited[nx][ny] = turn
                    if g[nx][ny] != '0':# 1이나 # 이라면, 다음 턴에서 반복. 따라서 loop에 append
                        g[nx][ny] = '0' # 0을 할당.
                        loop.append((nx,ny))
                    else:# 0이라면 1 만날 때 까지 반복. 따라서 q에 append.
                        q.append((nx,ny))
        q = loop# 다시 다음 턴을 진행하기 위해 q에 loop할당.
    return visited[x2][y2] 
    
    
print(bfs(x1,y1))
# 백준 주난의 난
# 2가지의 경우에 따라 로직이 다름. 2개의 큐를 이용.