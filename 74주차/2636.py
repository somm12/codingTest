from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
g = []
initCnt = 0
for i in range(n):
    g.append(list(map(int,input().split())))
   

cnt = []# 치즈 개수 리스트.
dx = [-1,1,0,0]# 상 하 좌 우
dy = [0,0,-1,1]


while True:
    q = deque()
    q.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] =1
    total = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+ dx[i],y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if g[nx][ny] == 0:# 빈공간에 둘러쌓인 치즈를 찾기 위해 0인 부분 bfs
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                else:#1이면 곧 사라질 치즈. 현재 턴에서 치즈 개수를 세고, 방문처리 하고 0으로 만듦.
                    total += 1
                    visited[nx][ny] = 1
                    g[nx][ny] = 0
    
    cnt.append(total)
    # 녹고 남은 치즈 총 개수 세기.
    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                count += 1
    
    if count == 0:# 모두 녹으면 끝.
        break

print(len(cnt))# 모두 녹는데 걸린 시간
print(cnt[-1])# 모두 녹기 한 시간 전의 치즈 개수.
# 치즈
